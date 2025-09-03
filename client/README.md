# Mi CV Optimizer - Frontend

Aplicación web React para la interfaz de usuario del optimizador de CVs con inteligencia artificial.

## 🎯 Propósito

El frontend proporciona una interfaz intuitiva y amigable que permite a los usuarios:
- Subir archivos PDF de sus CVs
- Visualizar el progreso del procesamiento
- Ver el texto optimizado generado por la IA
- Descargar el CV mejorado en formato PDF

## 🛠️ Tecnologías Utilizadas

- **React 19.0.0** - Framework principal para la UI
- **JavaScript (ES6+)** - Lenguaje de programación
- **CSS3** - Estilos y diseño responsivo
- **Axios** - Cliente HTTP para comunicación con la API
- **Create React App** - Herramientas de build y desarrollo
- **React Testing Library** - Framework de testing
- **Web Vitals** - Métricas de rendimiento web

### Dependencias Principales

```json
{
  "react": "^19.0.0",
  "react-dom": "^19.0.0",
  "axios": "^1.6.0",
  "react-scripts": "5.0.1"
}
```

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Node.js (versión 16 o superior)
- npm (viene con Node.js)

### Instalación

1. **Navegar al directorio del cliente:**
```bash
cd client
```

2. **Instalar dependencias:**
```bash
npm install
```

### Comandos Disponibles

#### `npm start`
Ejecuta la aplicación en modo desarrollo.
- Abre automáticamente [http://localhost:3000](http://localhost:3000)
- La página se recarga automáticamente cuando realizas cambios
- Los errores de lint aparecen en la consola

#### `npm test`
Lanza el runner de pruebas en modo interactivo.
- Ejecuta todas las pruebas disponibles
- Modo watch activado por defecto

#### `npm run build`
Construye la aplicación para producción en la carpeta `build/`.
- Optimiza el build para mejor rendimiento
- Los archivos son minificados
- Los nombres de archivo incluyen hashes para cache-busting

#### `npm run eject`
**⚠️ Nota: Esta es una operación irreversible!**

Expone todas las configuraciones de Create React App para personalización avanzada.

## 📁 Estructura del Código

```
client/
├── public/
│   ├── index.html          # Template HTML principal
│   └── manifest.json       # Configuración PWA
├── src/
│   ├── App.js              # Componente principal
│   ├── App.css             # Estilos principales
│   ├── index.js            # Punto de entrada
│   ├── setupTests.js       # Configuración de pruebas
│   └── reportWebVitals.js  # Métricas de rendimiento
├── package.json            # Dependencias y scripts
└── README.md               # Este archivo
```

## 🎨 Funcionalidades de la UI

### Componente Principal (App.js)

- **Subida de archivos**: Interfaz drag & drop para PDFs
- **Barra de progreso**: Indicador visual del procesamiento
- **Vista previa**: Muestra el texto optimizado
- **Descarga**: Botón para descargar el PDF mejorado
- **Manejo de errores**: Alertas informativas para el usuario

### Estilos (App.css)

- **Diseño responsivo**: Adaptable a diferentes tamaños de pantalla
- **UI/UX intuitiva**: Interfaz limpia y profesional
- **Animaciones**: Transiciones suaves para mejor experiencia
- **Accesibilidad**: Cumple estándares de accesibilidad web

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` en el directorio client/ para configuraciones:

```env
REACT_APP_API_URL=http://localhost:5000
REACT_APP_VERSION=1.0.0
```

### Configuración de API

El frontend se comunica con el backend Flask en las siguientes rutas:
- `POST /process` - Procesar CV
- `POST /download` - Descargar PDF optimizado

## 🧪 Testing

### Ejecutar Pruebas

```bash
npm test
```

### Estructura de Pruebas

- **App.test.js** - Pruebas del componente principal
- **setupTests.js** - Configuración global de testing

### Coverage

Para generar reporte de cobertura:
```bash
npm test -- --coverage --watchAll=false
```

## 🚢 Build y Deployment

### Build para Producción

```bash
npm run build
```

El build optimizado se genera en la carpeta `build/` y está listo para deployment.

### Deployment

El frontend puede ser deployado en:
- **Netlify**: Conecta el repositorio directamente
- **Vercel**: Deploy automático desde Git
- **GitHub Pages**: Para hosting estático
- **Heroku**: Junto con el backend

### Configuración para Heroku

Para deploy conjunto con el backend, el build se debe servir estáticamente desde Flask.

## 📱 Responsive Design

La aplicación está optimizada para:
- **Desktop**: Resoluciones 1920x1080 y superiores
- **Tablet**: 768px - 1024px
- **Mobile**: 375px - 767px

## 🔒 Seguridad

- **Validación de archivos**: Solo acepta PDFs
- **Sanitización**: Limpieza de inputs del usuario
- **HTTPS**: Preparado para conexiones seguras
- **CORS**: Configurado para dominios específicos

## 🎯 Roadmap

### Próximas Funcionalidades
- [ ] Drag & drop mejorado
- [ ] Preview del PDF original
- [ ] Comparación lado a lado
- [ ] Temas de interfaz (claro/oscuro)
- [ ] Internacionalización (i18n)

## 🐛 Troubleshooting

### Problemas Comunes

**Error: "npm start" no funciona**
```bash
rm -rf node_modules package-lock.json
npm install
npm start
```

**Error de CORS**
- Verificar que el backend esté ejecutándose
- Confirmar URL del API en el código

**Error de build**
```bash
npm run build -- --verbose
```

## 🤝 Contribución

1. Sigue las convenciones de React
2. Usa componentes funcionales con hooks
3. Mantén la accesibilidad web
4. Incluye pruebas para nuevas funcionalidades
5. Documenta cambios significativos

## 📚 Recursos Adicionales

- [Documentación de React](https://reactjs.org/)
- [Create React App](https://create-react-app.dev/)
- [Testing Library](https://testing-library.com/)
- [Axios Documentation](https://axios-http.com/)

---

Para más información sobre el proyecto completo, consulta el [README principal](../README.md).