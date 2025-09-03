# Mi CV Optimizer - Backend

API REST desarrollada en Flask que utiliza inteligencia artificial para procesar y optimizar currículums vitae.

## 🎯 Propósito

El backend proporciona la lógica de procesamiento y API que permite:
- Recibir archivos PDF de CVs desde el frontend
- Extraer texto de documentos PDF
- Procesar el contenido con modelos de IA
- Generar versiones optimizadas de los CVs
- Crear y entregar PDFs mejorados

## 🛠️ Tecnologías Utilizadas

### Framework y Core
- **Python 3.8+** - Lenguaje de programación principal
- **Flask** - Framework web minimalista y flexible
- **Flask-CORS** - Manejo de Cross-Origin Resource Sharing

### Inteligencia Artificial
- **Transformers** - Biblioteca de Hugging Face para modelos de NLP
- **PyTorch** - Framework de machine learning para IA
- **Hugging Face Models** - Modelos preentrenados para optimización de texto

### Procesamiento de Documentos
- **pdfminer.six** - Extracción de texto de archivos PDF
- **FPDF** - Generación de documentos PDF
- **Werkzeug** - Utilidades WSGI para manejo de archivos

### Infraestructura
- **Docker** - Containerización (Dockerfile incluido)
- **Heroku** - Platform as a Service para deployment

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Navegar al directorio del servidor:**
```bash
cd server
```

2. **Crear entorno virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requeriments.txt
```

### Ejecución

#### Modo Desarrollo
```bash
cd src
python app.py
```

El servidor estará disponible en `http://localhost:5000`

#### Modo Producción
```bash
cd src
python app.py
```

### Docker

#### Construir imagen
```bash
docker build -t mi-cv-optimizer-backend .
```

#### Ejecutar contenedor
```bash
docker run -p 5000:5000 mi-cv-optimizer-backend
```

## 📁 Estructura del Código

```
server/
├── src/
│   ├── app.py              # Aplicación principal Flask
│   ├── routes.py           # Definición de rutas de la API
│   ├── config.py           # Configuración de la aplicación
│   └── helpers.py          # Funciones auxiliares
├── requeriments.txt        # Dependencias de Python
├── Dockerfile              # Configuración de Docker
└── README.md               # Este archivo
```

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` en el directorio server/ para configuraciones:

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=tu_clave_secreta_aqui
MAX_CONTENT_LENGTH=16777216  # 16MB máximo para archivos
UPLOAD_FOLDER=uploads
```

### config.py

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB máximo
    UPLOAD_FOLDER = 'uploads'
```

## 🛡️ API Endpoints

### GET /
**Descripción**: Endpoint de bienvenida y health check

**Respuesta**:
```json
{
    "message": "Bienvenido a la API de OptimizaCV. Usa /process para optimizar tu CV y /download para descargarlo."
}
```

### POST /process
**Descripción**: Procesa un CV en formato PDF y retorna el texto optimizado

**Parámetros**:
- `cv` (file): Archivo PDF del currículum

**Respuesta exitosa**:
```json
{
    "improved_text": "Texto del CV optimizado por IA...",
    "status": "success"
}
```

**Errores**:
- `400`: Archivo no válido o no es un CV
- `500`: Error interno del servidor

### POST /download
**Descripción**: Genera y descarga un PDF con el texto optimizado

**Parámetros**:
```json
{
    "improved_text": "Texto optimizado a convertir en PDF"
}
```

**Respuesta**: Archivo PDF para descarga

## 🧠 Procesamiento de IA

### Flujo de Procesamiento

1. **Extracción**: `extract_text_from_pdf()` - Extrae texto del PDF
2. **Validación**: `is_cv()` - Verifica que sea un CV válido
3. **Optimización**: `improve_cv_text()` - Aplica IA para mejorar el contenido
4. **Generación**: `create_pdf_from_text()` - Crea PDF optimizado

### Modelos de IA

```python
# helpers.py - Función de mejora con IA
def ai_improver(text):
    # Implementación con transformers
    # Utiliza modelos de Hugging Face para NLP
    pass
```

## 🔒 Seguridad

### Validación de Archivos
```python
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}
```

### Sanitización
- Validación de tipos de archivo
- Límites de tamaño de archivo (16MB)
- Sanitización de nombres de archivo con `secure_filename()`

### CORS
```python
# Configurado para permitir requests desde el frontend
CORS(app, origins=["http://localhost:3000"])
```

## 📊 Dependencias Detalladas

### requeriments.txt
```txt
Flask                 # Framework web
flask-cors           # Cross-Origin Resource Sharing
pdfminer.six         # Extracción de texto PDF
transformers         # Modelos de IA de Hugging Face
torch                # Framework de machine learning
fpdf                 # Generación de PDFs
```

### Instalación de Dependencias Adicionales

Para desarrollo:
```bash
pip install pytest flask-testing
```

Para producción:
```bash
pip install gunicorn
```

## 🧪 Testing

### Estructura de Pruebas
```bash
server/
├── tests/
│   ├── test_app.py         # Pruebas de la aplicación
│   ├── test_routes.py      # Pruebas de endpoints
│   └── test_helpers.py     # Pruebas de funciones auxiliares
```

### Ejecutar Pruebas
```bash
pytest tests/
```

### Coverage
```bash
pytest --cov=src tests/
```

## 🚢 Deployment

### Heroku

1. **Configurar Procfile** (ya incluido):
```
web: python server/src/app.py
```

2. **Deploy**:
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requeriments.txt .
RUN pip install -r requeriments.txt

COPY src/ .
EXPOSE 5000

CMD ["python", "app.py"]
```

### Variables de Entorno en Producción

```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=tu_clave_secreta_produccion
```

## 🔧 Configuración Avanzada

### Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)
```

## 🔄 API de Desarrollo

### Modo Debug
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

### Hot Reload
Flask en modo debug recarga automáticamente al detectar cambios.

## 📈 Monitoreo

### Health Check
```bash
curl http://localhost:5000/
```

### Logs
```bash
tail -f app.log
```

## 🐛 Troubleshooting

### Problemas Comunes

**Error: ModuleNotFoundError**
```bash
pip install -r requeriments.txt
```

**Error: Puerto en uso**
```bash
lsof -ti:5000 | xargs kill -9
```

**Error de permisos con archivos**
```bash
chmod 755 uploads/
```

**Error de memoria con modelos de IA**
- Verificar RAM disponible
- Considerar modelos más pequeños

## 🎯 Roadmap

### Próximas Funcionalidades
- [ ] Cache de resultados de IA
- [ ] Múltiples idiomas
- [ ] API versioning
- [ ] Rate limiting avanzado
- [ ] Métricas y analytics
- [ ] Base de datos para persistencia

## 🤝 Contribución

1. Sigue PEP 8 para estilo de código Python
2. Incluye docstrings en todas las funciones
3. Añade pruebas para nuevas funcionalidades
4. Actualiza la documentación de API

## 📚 Recursos Adicionales

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [pdfminer.six Documentation](https://pdfminersix.readthedocs.io/)

---

Para más información sobre el proyecto completo, consulta el [README principal](../README.md).