# Mi CV Optimizer

Una aplicación web inteligente que utiliza inteligencia artificial para optimizar currículums vitae (CVs) y ayudar a los usuarios a mejorar sus oportunidades laborales.

## 🎯 Propósito del Proyecto

Mi CV Optimizer es una herramienta que permite a los usuarios:
- Subir su CV en formato PDF
- Procesarlo con inteligencia artificial para identificar áreas de mejora
- Recibir una versión optimizada del CV con sugerencias y mejoras
- Descargar el CV mejorado en formato PDF

La aplicación está diseñada para ayudar a profesionales a destacar en el mercado laboral mediante la optimización automatizada de sus currículums.

## 🛠️ Tecnologías Utilizadas

### Frontend (Cliente)
- **React 19.0.0** - Framework de JavaScript para la interfaz de usuario
- **JavaScript (ES6+)** - Lenguaje de programación principal
- **CSS3** - Estilos y diseño responsivo
- **Axios** - Cliente HTTP para comunicación con la API
- **Create React App** - Herramienta de configuración y build

### Backend (Servidor)
- **Python** - Lenguaje de programación principal
- **Flask** - Framework web minimalista
- **Flask-CORS** - Manejo de CORS para comunicación entre dominios
- **Transformers** - Biblioteca de Hugging Face para procesamiento de IA
- **PyTorch** - Framework de machine learning
- **pdfminer.six** - Extracción de texto de archivos PDF
- **FPDF** - Generación de archivos PDF
- **Werkzeug** - Utilidades WSGI

### Infraestructura y Deployment
- **Heroku** - Plataforma de deployment (configurado con Procfile)
- **Docker** - Containerización (Dockerfile incluido)

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Node.js (versión 16 o superior)
- Python 3.8 o superior
- npm o yarn

### Configuración del Proyecto

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Dieg0bl/mi-cv-optimizer.git
cd mi-cv-optimizer
```

2. **Configurar el Backend:**
```bash
cd server
pip install -r requeriments.txt
cd src
python app.py
```
El servidor estará disponible en `http://localhost:5000`

3. **Configurar el Frontend:**
```bash
cd client
npm install
npm start
```
La aplicación estará disponible en `http://localhost:3000`

### Ejecución en Desarrollo

Para ejecutar la aplicación completa en modo desarrollo:

1. **Terminal 1 - Backend:**
```bash
cd server/src
python app.py
```

2. **Terminal 2 - Frontend:**
```bash
cd client
npm start
```

### Build para Producción

**Frontend:**
```bash
cd client
npm run build
```

**Backend:**
El backend está listo para producción. Para deployment en Heroku, el Procfile ya está configurado.

## 📁 Estructura del Proyecto

```
mi-cv-optimizer/
├── client/                 # Aplicación React (Frontend)
│   ├── src/               # Código fuente del frontend
│   ├── public/            # Archivos públicos
│   └── package.json       # Dependencias del frontend
├── server/                # API Flask (Backend)
│   ├── src/              # Código fuente del backend
│   ├── requeriments.txt  # Dependencias de Python
│   └── Dockerfile        # Configuración de Docker
├── Procfile              # Configuración para Heroku
└── README.md             # Este archivo
```

## 🔧 Scripts Disponibles

### Frontend (client/)
- `npm start` - Ejecuta la app en modo desarrollo
- `npm test` - Ejecuta las pruebas
- `npm run build` - Construye la app para producción
- `npm run eject` - Expone configuraciones de Create React App

### Backend (server/)
- `python app.py` - Ejecuta el servidor Flask
- `pip install -r requeriments.txt` - Instala dependencias

## 🌐 Deployment

La aplicación está configurada para deployment en Heroku:
1. El `Procfile` especifica cómo ejecutar la aplicación
2. El frontend debe ser construido y servido estáticamente
3. El backend maneja la API y el procesamiento de IA

## 📝 Uso de la Aplicación

1. Accede a la aplicación web
2. Selecciona un archivo PDF de tu CV
3. Haz clic en "Subir y Optimizar"
4. Espera mientras la IA procesa tu CV
5. Revisa el texto optimizado generado
6. Descarga tu CV mejorado en formato PDF

## 🔒 Privacidad y Seguridad

La aplicación está diseñada para proteger la privacidad de los usuarios:
- Los archivos PDF se procesan temporalmente
- No se almacenan datos personales permanentemente
- Se garantiza la confidencialidad de la información del CV

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

© 2025 Optimiza tu CV. Protegemos tus datos y garantizamos tu privacidad.
