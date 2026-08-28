import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from google import genai
from sqlalchemy.orm import Session

from backend.database import Base, engine, get_db
from backend.models import BlogPost
from backend.schemas import BlogCreate, BlogResponse

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Blog Generator API")

# Pasa la clave directamente al cliente para evitar problemas de lectura
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")
client = genai.Client(api_key=GEMINI_KEY)


@app.post("/generate-blog/", response_model=BlogResponse)
def generate_blog(blog_input: BlogCreate, db: Session = Depends(get_db)):
    try:
        # 1. Generar texto con Gemini
        prompt = (
            f"Escribe un artículo de blog completo y estructurado en Markdown "
            f"sobre el tema: '{blog_input.topic}'. El tono debe ser {blog_input.tone}. "
            f"Incluye un título en la primera línea comenzando con #"
        )

        response = client.models.generate_content(
        model="gemini-3.6-flash",
    contents=prompt,
)

        full_text = response.text

        # Separar título del cuerpo
        lines = full_text.split("\n")
        title = (
            lines[0].replace("#", "").strip()
            if lines
            else f"Artículo sobre {blog_input.topic}"
        )
        content = "\n".join(lines[1:]).strip()

        # 2. Imagen conceptual mediante URL dinámica
        image_url = f"https://picsum.photos/1024/600?random={abs(hash(blog_input.topic)) % 1000}"

        # 3. Guardar en Base de Datos
        new_post = BlogPost(
            title=title,
            content=content,
            image_url=image_url,
            tone=blog_input.tone,
        )
        db.add(new_post)
        db.commit()
        db.refresh(new_post)

        return new_post

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/posts/", response_model=list[BlogResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(BlogPost).order_by(BlogPost.id.desc()).all()