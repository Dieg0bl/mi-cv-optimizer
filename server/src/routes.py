from flask import Blueprint, request, jsonify, send_file
import os, time
from werkzeug.utils import secure_filename
from helpers import (
    allowed_file,
    extract_text_from_pdf,
    is_cv,
    improve_cv_text,
    create_pdf_from_text,
    ai_improver
)
from config import Config

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Bienvenido a la API de OptimizaCV. Usa /process para optimizar tu CV y /download para descargarlo."
    })

@routes.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "La API está funcionando correctamente."})

@routes.route("/status", methods=["GET"])
def model_status():
    status = "cargado" if ai_improver else "no disponible"
    return jsonify({"model_status": status})

@routes.route('/process', methods=['POST'])
def process_cv_route():
    if 'cv' not in request.files:
        return jsonify({'error': 'No se encontró el archivo en la solicitud'}), 400

    file = request.files['cv']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'El archivo debe ser un PDF válido'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        extracted_text = extract_text_from_pdf(filepath)
        if not extracted_text or not extracted_text.strip():
            os.remove(filepath)
            return jsonify({'error': 'No se pudo extraer texto del PDF. Asegúrate de que el archivo contenga texto seleccionable.'}), 400

        if not is_cv(extracted_text):
            os.remove(filepath)
            return jsonify({'error': 'El archivo no parece ser un CV válido.'}), 400

        time.sleep(2)
        improved_text = improve_cv_text(extracted_text, ai_improver)
        os.remove(filepath)
        return jsonify({'improved_text': improved_text})
    except Exception as e:
        print("❌ Excepción en process_cv_route:", e)
        return jsonify({'error': f'Error al procesar el archivo: {str(e)}'}), 500

@routes.route('/download', methods=['POST'])
def download_pdf_route():
    data = request.get_json()
    improved_text = data.get('improved_text', '')
    if not improved_text:
        return jsonify({'error': 'No se proporcionó texto optimizado'}), 400

    pdf_file = create_pdf_from_text(improved_text)
    if not pdf_file:
        return jsonify({'error': 'Error interno al generar el PDF'}), 500

    return send_file(pdf_file, as_attachment=True, download_name="CV_optimizado.pdf", mimetype='application/pdf')
