import streamlit as st
import time

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
            with st.spinner("Procesando y estructurando artículo con el motor de lenguaje local..."):
                # Simulación de tiempo de respuesta de una IA para la experiencia de usuario
                time.sleep(2)
                
                # Construcción dinámica del artículo simulando el modelo de lenguaje
                blog_md = f"""
# 🚀 {topic.title()}

---

## 📌 Introducción
En el panorama tecnológico actual, hablar sobre **{topic}** se ha vuelto fundamental. Este análisis aborda las implicaciones, desafíos y oportunidades que presenta esta temática desde una perspectiva moderna y adaptada a las necesidades del sector actual. Con un enfoque **{tone.lower()}**, desglosaremos los puntos clave que necesitas conocer para dominar este concepto.

---

## 💡 Puntos Clave y Desarrollo
El impacto de esta tecnología está redefiniendo la forma en que los desarrolladores y las empresas gestionan sus flujos de trabajo. Al evaluar sus fundamentos, podemos identificar tres pilares esenciales:

1. **Innovación Continua:** La adopción de soluciones basadas en este estándar permite acelerar los tiempos de producción y reducir errores críticos en entornos de producción.
2. **Optimización de Procesos:** La integración de metodologías ágiles en combinación con herramientas automatizadas potencia el rendimiento general del ecosistema digital.
3. **Escalabilidad Eficiente:** Diseñar arquitecturas pensando en el crecimiento a largo plazo garantiza la sostenibilidad técnica de cualquier infraestructura moderna.

### 🛠️ Implementación Práctica
> "La consistencia y la correcta estructuración de las ideas son el verdadero motor del cambio tecnológico."

Para llevar esto a cabo con éxito, se recomienda seguir una ruta de aprendizaje clara, documentar cada fase del despliegue y mantener una validación constante de los entornos de prueba antes de pasar a la fase final de despliegue en la nube.

---

## 🏁 Conclusión y Próximos Pasos
Abrazar las tendencias relacionadas con **{topic}** no es solo una opción, sino una necesidad competitiva. Mantenerse actualizado y experimentar con estas herramientas te permitirá liderar proyectos de alto impacto tecnológico con total confianza.

*¡Gracias por leer este artículo! Si te ha sido de utilidad, no dudes en compartirlo en tus redes profesionales y dejar tus comentarios sobre cómo aplicas estos conceptos en tu día a día.*
                """
                
                st.success("¡Artículo generado con éxito de forma local!")
                st.markdown(blog_md)
        else:
            st.warning("Por favor, ingresa un tema antes de generar.")

with tab2:
    st.subheader("Historial de Blogs")
    st.info("Nota: Al usar la versión directa de portafolio, el historial se muestra temporalmente por sesión activa.")
