# Mi CV Optimizer

Herramienta simple para optimizar CV. Mejora automáticamente el contenido de tu currículum mediante procesamiento de texto inteligente.

## Instalación y Uso

### Requisitos
- Node.js 18+ 
- Python 3.8+

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Dieg0bl/mi-cv-optimizer.git
cd mi-cv-optimizer
```

2. Instala dependencias del cliente:
```bash
cd client
npm install
```

3. Instala dependencias del servidor:
```bash
cd ../server
pip install -r requirements.txt
```

### Uso

1. Inicia el servidor backend:
```bash
cd server/src
python app.py
```

2. En otra terminal, inicia el cliente web:
```bash
cd client
npm start
```

3. Abre http://localhost:3000 en tu navegador

4. Sube tu CV en formato PDF y obtén una versión optimizada

## Ejemplo

```bash
# Terminal 1 - Backend
cd server/src && python app.py

# Terminal 2 - Frontend  
cd client && npm start
```

Luego ve a http://localhost:3000, sube tu PDF y descarga el CV optimizado.

## Estado

**Estado: en desarrollo**

Funcionalidades actuales:
- ✅ Subida de archivos PDF
- ✅ Procesamiento de texto
- ✅ Descarga de CV optimizado
- 🔄 Mejoras de algoritmos en progreso

## Estructura

```
mi-cv-optimizer/
├── client/          # React frontend
├── server/          # Flask backend
└── README.md
```
