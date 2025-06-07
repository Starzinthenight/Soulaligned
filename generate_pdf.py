from fpdf import FPDF
import os

class SoulBlueprintPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return  # No header on cover
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, 'Your Soul Blueprint', ln=True, align='C')
        self.ln(10)

    def footer(self):
        if self.page_no() == 1:
            return  # No footer on cover
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(160, 132, 202)
        self.cell(0, 10, 'www.soulaligned.life  |  Awakened by Design', align='C')

    def add_section(self, title, content):
        if self.get_y() > 240:
            self.add_page()
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(160, 132, 202)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 9, content)
        self.ln(5)

def create_pdf(output_path, name, rooted, heart, expression, mental, awakened, life_path, destiny):
    pdf = SoulBlueprintPDF()

    # COVER PAGE
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 20)
    pdf.set_text_color(160, 132, 202)
    pdf.cell(0, 20, f"{name}'s Soul Blueprint", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(0, 0, 0)
    cover_message = (
        "This document is a sacred reflection of your essence, potential, and personal magic.\n\n"
        "It has been lovingly created to guide you back to your truth and support your growth."
    )
    pdf.multi_cell(0, 10, cover_message)
    pdf.ln(10)

    # DEDICATION PAGE
    pdf.add_page()
    pdf.set_font('Helvetica', '', 12)
    dedication = (
        f"Dear {name},\n\n"
        "This Soul Blueprint has been lovingly created to illuminate your inner world and guide you back to your authentic self. "
        "May it bring clarity, strength, and a deeper connection to your soul path.\n\n"
        "With love,\nSoul Aligned\n\n"
    )
    pdf.multi_cell(0, 9, dedication)
    pdf.ln(5)

    # SECTIONS
    pdf.add_section("Rooted Foundation", f"{rooted}\n\nYour Rooted Foundation is your raw energy, your basic instinctual vibration, the steady pulse beneath your action. When life feels chaotic or uncertain, this energy needs to be grounded. It reflects the way you initiate, move, and protect what matters. This is the realm of the instinctual self, the part of you that knows without needing to explain. Honour this foundation by trusting your instincts and embracing your intrinsic qualities as you move forward with purpose.")

    pdf.add_section("Heart of Connection", f"{heart}\n\nThe Heart of Connection is where your emotional landscape lives, how you receive, nurture, and bond. It speaks to the way you build intimacy with both yourself and others. Here lies your capacity to hold, soften, and respond with care. It is believed our emotional life reveals what we truly value. Your heart energy is a sacred space: protect it, honour it, and let it guide you toward relationships that reflect your soul’s truth.")

    pdf.add_section("Self Expression", f"{expression}\n\nYour Self Expression is the spark of your individuality, how your inner fire becomes visible to the world. This energy holds your vitality, your radiance, and your creative essence. This area governs the process of becoming more whole by embracing your true self. This is where your gifts want to be seen and shared. Express not for approval, but for alignment.")

    pdf.add_section("Mental Mastery", f"{mental}\n\nMental Mastery reveals how you think, speak, and interpret the world around you. It’s not about intellect alone, it’s about clarity, communication, and how your thoughts shape your reality. This is your conscious voice, your perception filter, and the part of you that makes meaning from experience. Until you make the unconscious conscious, it will direct your life and you will call it fate. Let this section guide you toward greater self-awareness and mental freedom.")

    pdf.add_section("Awakened Self", f"{awakened}\n\nThe Awakened Self is the evolving you, the self that emerges through transformation, reflection, and soul initiation. It blends your outward path with your inner growth, revealing the character you are becoming. It holds potential, identity, and purpose, not fixed, but always unfolding. Our awakened self embraces the totality of conscious and unconscious aspects within us. This is your invitation to live more fully as you, align and explore both aspects of yourself, bringing you into a place of wholeness.")

    pdf.add_section("Life Path", f"{life_path}\n\nYour Life Path number reveals your life theme, the lessons you are here to embody and the experiences you are meant to explore. It’s the heartbeat of your soul’s evolution in this lifetime. This number offers you insight into the patterns that repeat and the strengths that anchor you. It’s less about prediction and more about purpose. Lean into its message with curiosity, and trust that your path is shaped by both design and desire.")

    pdf.add_section("Destiny Number", f"{destiny}\n\nYour Destiny Number reveals the soul qualities you are called to express. It reflects the archetype you are here to grow into, a spiritual imprint of your inner calling. It doesn’t tell you who to be, but rather who you are becoming as you step more fully into wholeness. It speaks to your deeper integration, the path toward embodying your Self archetype in the world. Align with your Destiny by allowing your becoming to unfold without force.")

    # FINAL PAGE
    pdf.add_page()
    pdf.set_font('Helvetica', 'I', 14)
    pdf.set_text_color(100, 100, 100)
    closing = (
        "Thank you for exploring your Soul Blueprint.\n\n"
        "You are already everything you seek.\n\n"
        "Let this guide be a mirror of your brilliance — and a reminder to walk forward with heart, presence, and purpose.\n\n"
        "With infinite love,\nSoul Aligned"
    )
    pdf.multi_cell(0, 10, closing)

    # Save the file
    pdf.output(output_path)
