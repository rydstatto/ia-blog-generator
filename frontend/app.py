import streamlit as st
import os
from google import genai

st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("🤖 Generador Automatizado de Blogs con IA")
st.write("Crea artículos completos con imágenes optimizadas usando Inteligencia Artificial.")

# Crear pestañas para organizar la app
tab1, tab2 = st.tabs(["📝 Crear Artículo", "📚 Historial de Blogs"])

with tab1:
    st.subheader("Configura tu próximo artículo")
    topic = st.text_input(
        "¿De qué quieres que hable tu artículo?",
        placeholder="Ej. El futuro de Python en el desarrollo web"
    )
    
    tone = st.selectbox(
        "Selecciona el tono del artículo",
        ["Profesional", "Casual", "Informativo", "Creativo"]
    )
    
    if st.button("Generar Artículo"):
        if topic:
            with st.spinner("Generando artículo con Gemini..."):
                try:
                    # Inicializa el cliente usando la API Key de los Secrets de Streamlit
                    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
                    
                    # Llamada directa al modelo oficial actual de Google
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=f"Escribe un artículo de blog extenso, estructurado y optimizado para SEO sobre: '{topic}'. El tono debe ser {tone}."
                    )
                    
                    st.success("¡Artículo generado con éxito!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Hubo un problema al conectar con la IA: {e}")
                    st.info("Asegúrate de haber configurado tu GEMINI_API_KEY en los Secrets de Streamlit Cloud.")
        else:
            st.warning("Por favor, ingresa un tema antes de generar.")

with tab2:
    st.subheader("Historial de Blogs")
    st.info("Nota: Al usar la versión directa sin backend independiente, el historial se mostrará aquí temporalmente por sesión.")
