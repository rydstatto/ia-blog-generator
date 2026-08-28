import requests
import streamlit as st

st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("🤖 Generador Automatizado de Blogs con IA")
st.write(
    "Crea artículos completos con imágenes optimizadas usando Inteligencia Artificial."
)

# URLs de la API del Backend
BACKEND_URL = "http://127.0.0.1:8000"

# Crear pestañas para organizar la app
tab1, tab2 = st.tabs(["✨ Crear Artículo", "📚 Historial de Blogs"])

with tab1:
    st.subheader("Configura tu próximo artículo")
    topic = st.text_input(
        "¿De qué quieres que hable tu artículo?",
        placeholder="Ej. El futuro de Python en el desarrollo web",
    )
    tone = st.selectbox(
        "Selecciona el tono del contenido",
        ["Educativo", "Formal", "Divertido", "Persuasivo"],
    )

    if st.button("🚀 Generar Artículo Completo"):
        if not topic:
            st.warning("Por favor, introduce un tema.")
        else:
            with st.spinner(
                "La IA está redactando el texto y diseñando la imagen..."
            ):
                payload = {"topic": topic, "tone": tone}
                response = requests.post(
                    f"{BACKEND_URL}/generate-blog/", json=payload
                )

                if response.status_code == 200:
                    data = response.json()
                    st.success("¡Artículo generado con éxito!")

                    st.header(data["title"])
                    st.image(
                        data["image_url"],
                        caption="Imagen generada por DALL-E 3",
                        use_container_width=True,
                    )
                    st.markdown(data["content"])
                else:
                    st.error(f"Error al generar el blog: {response.text}")

with tab2:
    st.subheader("Artículos guardados")
    try:
        history_response = requests.get(f"{BACKEND_URL}/posts/")
        if history_response.status_code == 200:
            posts = history_response.json()
            for post in posts:
                with st.expander(f"📖 {post['title']} ({post['tone']})"):
                    st.image(post["image_url"], width=400)
                    st.markdown(post["content"])
        else:
            st.error("No se pudo cargar el historial.")
    except Exception:
        st.info("Inicia el backend para ver el historial.")