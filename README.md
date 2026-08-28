# 🤖 AI Blog Generator — FastAPI & Streamlit

[![Python Version](https://shields.io)](https://python.org)
[![FastAPI](https://shields.io)](https://tiangolo.com)
[![Streamlit](https://shields.io)](https://streamlit.io)
[![OpenAI](https://shields.io)](https://openai.com)

Un sistema de automatización de contenidos de extremo a extremo (End-to-End) que utiliza Inteligencia Artificial para la redacción y optimización SEO de artículos de blog, acompañados de imágenes de portada personalizadas y almacenamiento persistente de datos.

Este proyecto fue diseñado para demostrar el desarrollo de aplicaciones web modernas en Python, la integración robusta de modelos fundacionales (LLMs y modelos de difusión) y patrones arquitectónicos limpios.

---

## ✨ Características Principales

*   **Generación de Texto Avanzada (LLM):** Redacción automática de artículos completos con estructura semántica avanzada orientada a SEO, adaptándose a múltiples tonos (Educativo, Formal, Divertido, Persuasivo).
*   **Diseño de Portadas con IA:** Generación automatizada de imágenes de portada contextuales y de alta resolución para cada post a través de **DALL-E 3**.
*   **Arquitectura Desacoplada (Decoupled API):** Backend robusto con FastAPI que expone endpoints REST, separado por completo de una interfaz de usuario interactiva y fluida construida en Streamlit.
*   **Persistencia de Datos:** Sistema de almacenamiento local utilizando **SQLAlchemy ORM** y **SQLite** para la gestión del historial de publicaciones.

---

## 🛠️ Stack Tecnológico

*   **Backend:** Python 3.10+, FastAPI, Uvicorn.
*   **Frontend:** Streamlit, Requests.
*   **Inteligencia Artificial:** OpenAI API (GPT-4o y DALL-E 3).
*   **Base de Datos & ORM:** SQLite, SQLAlchemy, Pydantic (Validación de datos).

---

## 📐 Arquitectura del Proyecto

El proyecto sigue una estructura modular orientada a la separación de responsabilidades:

```text
ia-blog-generator/
├── backend/            # Lógica del servidor y API REST
│   ├── database.py     # Configuración y sesión del ORM
│   ├── main.py         # Endpoints de FastAPI e integración con la API de OpenAI
│   ├── models.py       # Modelos de tablas de la base de datos (SQLAlchemy)
│   └── schemas.py      # Esquemas de validación y tipado (Pydantic)
├── frontend/           # Interfaz de usuario interactiva
│   └── app.py          # Renderizado de componentes y consumo de la API local
├── .env                # Variables de entorno protegidas (Ignorado en Git)
├── .gitignore          # Filtro de archivos no deseados para control de versiones
└── requirements.txt    # Manifiesto de dependencias del entorno virtual
```

---

## 🚀 Instalación y Despliegue Local

### 1. Clonar el repositorio e ingresar a la carpeta
```bash
git clone https://github.com
cd ia-blog-generator
```

### 2. Configurar el Entorno Virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
.\venv\Scripts\activate

# Activar entorno (Mac/Linux)
source venv/bin/activate

# Instalar dependencias necesarias
pip install -r requirements.txt
```

### 3. Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura:
```env
OPENAI_API_KEY=tu_clave_api_aqui
DATABASE_URL=sqlite:///./blog.db
```

### 4. Ejecución del Sistema

Deberás iniciar el backend y el frontend en dos instancias o terminales diferentes (asegúrate de que ambas tengan el entorno virtual activo):

*   **Terminal 1 (Backend - FastAPI):**
    ```bash
    uvicorn backend.main:app --reload
    ```
    *La documentación interactiva de la API estará disponible en:* `http://127.0.0`

*   **Terminal 2 (Frontend - Streamlit):**
    ```bash
    streamlit run frontend/app.py
    ```
    *La aplicación web se abrirá automáticamente en tu navegador local.*

---

## 💡 Próximas Mejoras (Roadmap)
- [ ] Implementar autenticación y registro de usuarios mediante JWT tokens.
- [ ] Conexión directa mediante Webhooks para publicar automáticamente en WordPress o Medium.
- [ ] Migración del motor de base de datos local de SQLite a PostgreSQL en la nube.

---

## 📄 Licencia
Este proyecto se encuentra bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
