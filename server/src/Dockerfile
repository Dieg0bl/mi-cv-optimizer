# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY src/ ./src/
COPY config.py .
COPY helpers.py .
COPY routes.py .

# Expone el puerto que usa Flask
EXPOSE 5000

# Define la variable de entorno para Flask
ENV FLASK_APP=src/app.py

# Ejecuta la aplicación
CMD ["python", "src/app.py"]
