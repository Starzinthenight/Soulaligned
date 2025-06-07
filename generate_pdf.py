from fpdf import FPDF

def sanitize(text):
    try:
        return text.encode('latin-1', 'ignore').decode('latin-1')
    except Exception:
        return text  # fallback in worst-case

def create_pdf(
    output_path,
    name,
    rooted,
    heart,
    expression,
    mental,
    awakened,
    life_path,
    destiny
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, sanitize("Your Soul Blueprint"), ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", '', 12)

    # Each section with safe encoding
    pdf.multi_cell(0, 10, sanitize(f"Name: {name}"))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Rooted Foundation"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(rooted))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Heart of Connection"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(heart))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Self Expression"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(expression))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Mental Mastery"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(mental))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Awakened Self"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(awakened))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Life Path"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(life_path))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Destiny Number"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(destiny))

    pdf.output(output_path)
from fpdf import FPDF

def sanitize(text):
    try:
        return text.encode('latin-1', 'ignore').decode('latin-1')
    except Exception:
        return text  # fallback in worst-case

def create_pdf(
    output_path,
    name,
    rooted,
    heart,
    expression,
    mental,
    awakened,
    life_path,
    destiny
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, sanitize("Your Soul Blueprint"), ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", '', 12)

    # Each section with safe encoding
    pdf.multi_cell(0, 10, sanitize(f"Name: {name}"))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Rooted Foundation"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(rooted))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Heart of Connection"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(heart))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Self Expression"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(expression))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Mental Mastery"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(mental))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Awakened Self"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(awakened))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Life Path"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(life_path))
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, sanitize("Destiny Number"), ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, sanitize(destiny))

    pdf.output(output_path)
