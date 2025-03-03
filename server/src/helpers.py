import io
import re
import time
from transformers import pipeline
from pdfminer.high_level import extract_text
from fpdf import FPDF
from config import Config

# -----------------------------------------------------------------------------
# Cargar el modelo AI (T5-base) de Hugging Face, gratuito y de código abierto.
# -----------------------------------------------------------------------------
def load_model():
    """Carga el modelo AI para optimizar CVs."""
    try:
        print("Cargando modelo AI para optimización de CV...")
        model = pipeline("text2text-generation", model="t5-base")
        print("✅ Modelo AI cargado correctamente.")
        return model
    except Exception as e:
        print("❌ Error al cargar el modelo:", e)
        return None

# Cargar el modelo globalmente
ai_improver = load_model()

# -----------------------------------------------------------------------------
# Verificar si el archivo tiene una extensión permitida.
# -----------------------------------------------------------------------------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

# -----------------------------------------------------------------------------
# Extraer texto del PDF usando pdfminer.
# -----------------------------------------------------------------------------
def extract_text_from_pdf(filepath):
    try:
        print(f"Extrayendo texto del archivo: {filepath}")
        text = extract_text(filepath)
        print(f"✅ Texto extraído (primeros 200 caracteres): {text[:200]}")
        return text
    except Exception as e:
        print("❌ Error al extraer el texto del PDF:", e)
        return None

# -----------------------------------------------------------------------------
# Verificar si el texto se parece a un CV
# -----------------------------------------------------------------------------
def is_cv(text):
    keywords = ["experiencia", "educación", "perfil", "habilidades", "logros", "curriculum", "cv"]
    result = any(keyword in text.lower() for keyword in keywords)
    print(f"Verificación de CV: {'Sí' if result else 'No'}")
    return result

# -----------------------------------------------------------------------------
# Estandarizar la estructura del CV
# -----------------------------------------------------------------------------
def standardize_cv_text(text):
    pattern = re.compile(
        r'(?P<header>(?:Información\s+Personal|Perfil(?:\s+Profesional)?|Experiencia\s+Laboral|Educación|Habilidades|Idiomas|Otros))',
        re.IGNORECASE
    )
    splits = pattern.split(text)
    standardized = {
        "Información Personal": "",
        "Perfil Profesional": "",
        "Experiencia Laboral": "",
        "Educación": "",
        "Habilidades": "",
        "Idiomas": "",
        "Otros": ""
    }
    if splits and not pattern.match(splits[0]):
        standardized["Información Personal"] += splits[0].strip() + "\n"
    for i in range(1, len(splits), 2):
        header = splits[i].strip().title()
        content = splits[i+1].strip() if (i+1) < len(splits) else ""
        if "Información" in header:
            standardized["Información Personal"] += content + "\n"
        elif "Perfil" in header:
            standardized["Perfil Profesional"] += content + "\n"
        elif "Experiencia" in header:
            standardized["Experiencia Laboral"] += content + "\n"
        elif "Educación" in header:
            standardized["Educación"] += content + "\n"
        elif "Habilidades" in header:
            standardized["Habilidades"] += content + "\n"
        elif "Idiomas" in header:
            standardized["Idiomas"] += content + "\n"
        else:
            standardized["Otros"] += header + ": " + content + "\n"
    output = ""
    for section, content in standardized.items():
        if content.strip():
            output += f"==== {section} ====\n{content.strip()}\n\n"
    print("✅ CV estandarizado.")
    return output

# -----------------------------------------------------------------------------
# Optimizar el CV utilizando IA manteniendo el idioma original.
# -----------------------------------------------------------------------------
def improve_cv_text(text, model):
    standardized_text = standardize_cv_text(text)
    if model is None:
        return "Error: No se pudo cargar el modelo AI."
    cv_template = (
        "1. Información Personal (Nombre, contacto, dirección, etc.)\n"
        "2. Perfil Profesional (Resumen breve de experiencia y objetivos)\n"
        "3. Experiencia Laboral (Lista de roles, fechas en formato MM/AAAA o AAAA, logros cuantificables)\n"
        "4. Educación y Formación (Títulos, certificaciones)\n"
        "5. Habilidades y Competencias (Técnicas y blandas)\n"
        "6. Idiomas (Niveles de dominio)\n"
        "7. Otros Datos Relevantes"
    )
    prompt = (
        "Optimiza y reestructura el siguiente Curriculum Vitae. "
        "Mantén el idioma original y conserva todos los datos importantes. "
        "Utiliza la siguiente estructura para la salida:\n\n" + cv_template +
        "\n\nCurrículum Original:\n" + standardized_text +
        "\n\nDevuélveme únicamente el CV optimizado y reestructurado, sin explicaciones adicionales."
    )
    print("Enviando prompt a la IA para optimización...")
    try:
        improved = model(prompt, max_length=2048, do_sample=False)
        optimized_text = improved[0]['generated_text']
        print("✅ CV optimizado (primeros 200 caracteres):", optimized_text[:200])
        return optimized_text
    except Exception as e:
        print("❌ Error durante la optimización:", e)
        return text

# -----------------------------------------------------------------------------
# Generar un PDF a partir del texto optimizado
# -----------------------------------------------------------------------------
def create_pdf_from_text(text):
    try:
        print("Generando PDF optimizado...")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in text.split('\n'):
            pdf.multi_cell(0, 10, txt=line)
        pdf_output = io.BytesIO()
        pdf.output(pdf_output, 'F')
        pdf_output.seek(0)
        print("✅ PDF generado correctamente.")
        return pdf_output
    except Exception as e:
        print("❌ Error al generar el PDF:", e)
        return None
