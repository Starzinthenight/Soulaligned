import os
import unicodedata
from fpdf import FPDF
from PyPDF2 import PdfMerger

# Function to clean problematic Unicode characters
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = unicodedata.normalize("NFKD", text)
    replacements = {
        "\u2014": "-",   # em-dash
        "\u2013": "-",   # en-dash
        "\u2018": "'",   # left single quote
        "\u2019": "'",   # right single quote
        "\u201c": '"',   # left double quote
        "\u201d": '"',   # right double quote
        "\xa0": " ",     # non-breaking space
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text

# Custom PDF class using Helvetica (built-in font)
class BlueprintPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Helvetica", size=12)

    def add_section(self, title, text):
        title = clean_text(title)
        text = clean_text(text)
        self.set_font("Helvetica", style="B", size=14)
        self.multi_cell(0, 10, title)
        self.ln(2)
        self.set_font("Helvetica", size=12)
        self.multi_cell(0, 10, text)
        self.ln(5)

# PDF creation logic
def create_pdf(output_path, name, rooted, heart, expression, mental, awakened, life_path_text, destiny_text, life_path_number, destiny_number):
    base_pdf_path = "output/main_content.pdf"
    pdf = BlueprintPDF()
    pdf.add_section("Soul Blueprint for " + name, "")
    pdf.add_section("Step 1: Rooted Foundation", rooted)
    pdf.add_section("Step 2: Heart of Connection", heart)
    pdf.add_section("Step 3: Self Expression", expression)
    pdf.add_section("Step 4: Mental Mastery", mental)
    pdf.add_section("Step 5: Awakened Self", awakened)
     # Include number + meaning in the section titles
    pdf.add_section(f"Life Path Number: {life_path_number}", life_path_text)
    pdf.add_section(f"Destiny Number: {destiny_number}", destiny_text)

    merger = PdfMerger()
    merger.append("assets/cover_page.pdf")
    merger.append(base_pdf_path)
    merger.append("assets/thank_you_page.pdf")
    merger.write(output_path)
    merger.close()
