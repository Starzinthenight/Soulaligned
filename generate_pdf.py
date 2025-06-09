import os
from fpdf import FPDF
from PyPDF2 import PdfMerger

class BlueprintPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
        self.set_font("DejaVu", size=12)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

    def add_section(self, title, text):
        self.set_font("DejaVu", style="B", size=14)
        self.multi_cell(0, 10, title)
        self.ln(2)
        self.set_font("DejaVu", size=12)
        self.multi_cell(0, 10, text)
        self.ln(5)

def create_pdf(output_path, name, rooted, heart, expression, mental, awakened, life_path, destiny):
    base_pdf_path = "output/main_content.pdf"
    pdf = BlueprintPDF()
    pdf.add_section("Soul Blueprint for " + name, "")
    pdf.add_section("Step 1: Rooted Foundation", rooted)
    pdf.add_section("Step 2: Heart of Connection", heart)
    pdf.add_section("Step 3: Self Expression", expression)
    pdf.add_section("Step 4: Mental Mastery", mental)
    pdf.add_section("Step 5: Awakened Self", awakened)
    pdf.add_section("Life Path Number", life_path)
    pdf.add_section("Destiny Number", destiny)
    pdf.output(base_pdf_path)

    merger = PdfMerger()
    merger.append("assets/cover_page.pdf")
    merger.append(base_pdf_path)
    merger.append("assets/thank_you_page.pdf")
    merger.write(output_path)
    merger.close()
import os
from fpdf import FPDF
from PyPDF2 import PdfMerger

class BlueprintPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
        self.set_font("DejaVu", size=12)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

    def add_section(self, title, text):
        self.set_font("DejaVu", style="B", size=14)
        self.multi_cell(0, 10, title)
        self.ln(2)
        self.set_font("DejaVu", size=12)
        self.multi_cell(0, 10, text)
        self.ln(5)

def create_pdf(output_path, name, rooted, heart, expression, mental, awakened, life_path, destiny):
    base_pdf_path = "output/main_content.pdf"
    pdf = BlueprintPDF()
    pdf.add_section("Soul Blueprint for " + name, "")
    pdf.add_section("Step 1: Rooted Foundation", rooted)
    pdf.add_section("Step 2: Heart of Connection", heart)
    pdf.add_section("Step 3: Self Expression", expression)
    pdf.add_section("Step 4: Mental Mastery", mental)
    pdf.add_section("Step 5: Awakened Self", awakened)
    pdf.add_section("Life Path Number", life_path)
    pdf.add_section("Destiny Number", destiny)
    pdf.output(base_pdf_path)

    merger = PdfMerger()
    merger.append("assets/cover_page.pdf")
    merger.append(base_pdf_path)
    merger.append("assets/thank_you_page.pdf")
    merger.write(output_path)
    merger.close()
