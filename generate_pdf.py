import os
from fpdf import FPDF
from PyPDF2 import PdfMerger

class BlueprintPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

        # Register and use Unicode-safe font
        self.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
        self.set_font("DejaVu", "", 12)

    def add_section(self, title, text):
        self.set_font("DejaVu", "B", 14)
        self.multi_cell(0, 10, title)
        self.ln(2)
        self.set_font("DejaVu", "", 12)
        self.multi_cell(0, 10, text)
        self.ln(5)

def create_pdf(output_path, name, rooted, heart, expression, mental, awakened, life_path, destiny):
    # Step 1: Create main content PDF
    base_pdf_path = "output/main_content.pdf"
    os.makedirs("output", exist_ok=True)

    pdf = BlueprintPDF()
    pdf.add_section(f"Soul Blueprint for {name}", "")
    pdf.add_section("Step 1: Rooted Foundation", rooted)
    pdf.add_section("Step 2: Heart of Connection", heart)
    pdf.add_section("Step 3: Self Expression", expression)
    pdf.add_section("Step 4: Mental Mastery", mental)
    pdf.add_section("Step 5: Awakened Self", awakened)
    pdf.add_section("Life Path Number", life_path)
    pdf.add_section("Destiny Number", destiny)
    pdf.output(base_pdf_path)

    # Step 2: Merge cover, main content, and thank-you
    merger = PdfMerger()
    merger.append("assets/cover_page.pdf")
    merger.append(base_pdf_path)
    merger.append("assets/thank_you_page.pdf")
    merger.write(output_path)
    merger.close()
