from fpdf import FPDF
import os
from PyPDF2 import PdfMerger

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Soul Blueprint Report", 0, 1, "C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, title, ln=1)

    def chapter_body(self, text):
        self.set_font("Arial", "", 12)
        self.set_text_color(0)
        self.multi_cell(0, 10, text)
        self.ln()

    def add_section(self, title, text):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(text)

def create_pdf(output_path, name, rooted, heart, expression, mental, awakened, life_path, destiny):
    temp_path = os.path.join("output", "core_report.pdf")

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Soul Blueprint for {name}", ln=True, align="C")
    pdf.ln(10)

    pdf.add_section("Rooted Foundation", rooted)
    pdf.add_section("Heart of Connection", heart)
    pdf.add_section("Self Expression", expression)
    pdf.add_section("Mental Mastery", mental)
    pdf.add_section("Awakened Self", awakened)
    pdf.add_section("Life Path Number", life_path)
    pdf.add_section("Destiny Number", destiny)

    pdf.output(temp_path)

    # Merge with cover and closing page
    merger = PdfMerger()
    cover_path = os.path.join("assets", "cover_page.pdf")
    closing_path = os.path.join("assets", "thank_you_page.pdf")

    if os.path.exists(cover_path):
        merger.append(cover_path)
    merger.append(temp_path)
    if os.path.exists(closing_path):
        merger.append(closing_path)

    merger.write(output_path)
    merger.close()

    # Clean up temporary file
    os.remove(temp_path)
