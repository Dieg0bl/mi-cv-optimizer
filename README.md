# 🚀 CV Optimizer - Optimizador de Currículums con IA

**AI-powered CV/Resume optimizer that helps job seekers improve their resumes using Hugging Face Transformers**

## 📋 Descripción

CV Optimizer es una aplicación web que utiliza inteligencia artificial para mejorar y optimizar currículums vitae. Los usuarios pueden subir sus CVs en formato PDF y obtener una versión mejorada con mejor estructura, contenido optimizado y formato profesional, todo mientras se mantiene el idioma original del documento.

## ✨ Características Principales

- **🤖 IA Avanzada**: Utiliza el modelo T5-base de Hugging Face para optimización inteligente
- **📄 Procesamiento PDF**: Extrae y procesa texto de documentos PDF
- **🔧 Reestructuración Automática**: Organiza el contenido en secciones estandardizadas
- **🌐 Multiidioma**: Mantiene el idioma original del CV
- **📊 Mejoras Cuantificables**: Optimiza logros y experiencias con datos concretos
- **💼 Orientado a Resultados**: Diseñado para mejorar las posibilidades de éxito laboral

## 🛠️ Tecnologías

### Frontend
- **React 19.0.0** - Interfaz de usuario moderna y reactiva
- **Axios** - Cliente HTTP para comunicación con el backend
- **CSS3** - Estilos personalizados y responsive design

### Backend
- **Python 3.x** - Lenguaje principal del servidor
- **Flask** - Framework web ligero y eficiente
- **Hugging Face Transformers** - Modelos de IA para procesamiento de lenguaje natural
- **PyTorch** - Framework de machine learning
- **pdfminer.six** - Extracción de texto de archivos PDF
- **fpdf** - Generación de documentos PDF optimizados

### Deployment
- **Heroku** - Plataforma de hosting en la nube
- **Dominio personalizado** - optimizacv.com

## 🚀 Instalación y Uso

### Prerequisitos
- Node.js (v14 o superior)
- Python 3.x
- pip (gestor de paquetes de Python)

### Frontend (React)
```bash
cd client
npm install
npm start
```

### Backend (Flask)
```bash
cd server
pip install -r requeriments.txt
python src/app.py
```

## 📱 Cómo Funciona

1. **Subida de CV**: El usuario sube su CV en formato PDF
2. **Extracción de Texto**: El sistema extrae y analiza el contenido
3. **Validación**: Verifica que el documento sea un CV válido
4. **Optimización IA**: El modelo T5-base mejora la estructura y contenido
5. **Generación PDF**: Crea un nuevo PDF optimizado para descarga

## 🎯 Casos de Uso

- **Profesionales en búsqueda de empleo** que quieren mejorar sus CVs
- **Estudiantes** que necesitan estructurar mejor su experiencia académica
- **Reclutadores** que buscan estandarizar formatos de CVs
- **Consultores de carrera** que ayudan a clientes a optimizar sus perfiles

## 🔐 Privacidad y Seguridad

- Los archivos se procesan temporalmente y se eliminan después del procesamiento
- No se almacenan datos personales ni CVs en el servidor
- Cumplimiento con estándares de privacidad y protección de datos

## 🌟 Demo

Visita [optimizacv.com](https://optimizacv.com) para probar la aplicación en vivo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de crear un pull request.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**Desarrollado con ❤️ para ayudar a profesionales a conseguir mejores oportunidades laborales**
