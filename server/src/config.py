import os

class Config:
    # Carpeta donde se guardarán temporalmente los archivos subidos
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'server', 'uploads')
    ALLOWED_EXTENSIONS = {'pdf'}
    DEBUG = False  # Para producción, desactiva debug

if not os.path.exists(Config.UPLOAD_FOLDER):
    os.makedirs(Config.UPLOAD_FOLDER)
