import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("🤖 Generador Automatizado de Blogs con IA")
st.write("Crea artículos completos con imágenes optimizadas usando Inteligencia Artificial.")

# Configuración forzada de la clave API para compatibilidad regional
if "GEMINI_API_KEY" in os.environ:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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
                    # Usamos el modelo clásico pro/flash compatible con el backend anterior
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    response = model.generate_content(
                        f"Escribe un artículo de blog extenso, estructurado y optimizado para SEO sobre: '{topic}'. El tono debe ser {tone}."
                    )
                    
                    st.success("¡Artículo generado con éxito!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Hubo un problema al conectar con la IA: {e}")
                    st.info("Revisa la consola si el error de credenciales persiste.")
        else:
            st.warning("Por favor, ingresa un tema antes de generar.")

with tab2:
    st.subheader("Historial de Blogs")
    st.info("Nota: Al usar la versión directa sin backend independiente, el historial se mostrará aquí temporalmente por sesión.")
