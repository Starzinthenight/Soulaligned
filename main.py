import os
import uuid
from flask import Flask, request, render_template
from dotenv import load_dotenv
import blueprint_utils
import segments_loader
from generate_pdf import create_pdf
from email_utils import send_email_with_attachment

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='templates')

@app.route('/generate', methods=['POST'])
def generate():
    # 1) Collect user inputs from form
    name       = request.form.get('fullName', '').strip()
    email      = request.form.get('email', '').strip()
    birthdate  = request.form.get('birthDate', '')
    birthtime  = request.form.get('birthTime', '')
    birthplace = request.form.get('placeOfBirth', '').strip()

    # 2) Create report and load descriptive segments
    report = blueprint_utils.create_report(name, birthdate, birthtime, birthplace)
    segments = segments_loader.load_segments()

    # OPTIONAL: Emoji debugging
    for key, value in segments.items():
        if any(ord(char) > 255 for char in value):
            print(f"[EMOJI DETECTED] {key}: {value}")

    # 3) Retrieve blueprint descriptions (fallback if not found)
    rooted     = segments.get(f"mars_{report['chart']['mars_sign'].lower()}", f"Mars in {report['chart']['mars_sign']}")
    heart      = segments.get(f"moon_{report['chart']['moon_sign'].lower()}", f"Moon in {report['chart']['moon_sign']}")
    expression = segments.get(f"sun_{report['chart']['sun_sign'].lower()}", f"Sun in {report['chart']['sun_sign']}")
    mental     = segments.get(f"mercury_{report['chart']['mercury_sign'].lower()}", f"Mercury in {report['chart']['mercury_sign']}")
    awakened   = segments.get(f"ascendant_{report['chart']['ascendant_sign'].lower()}", f"Ascendant in {report['chart']['ascendant_sign']}")

    # 4) Numerology text
    lp = report['life_path']
    dn = report['destiny_number']
    life_path_text = segments.get(f"life_path_{lp}", f"Your Life Path Number is {lp}.")
    destiny_text   = segments.get(f"destiny_{dn}", f"Your Destiny Number is {dn}.")

    # 5) Generate the PDF
    pdf_filename = f"soul_blueprint_{uuid.uuid4().hex}.pdf"
    output_path = os.path.join("output", pdf_filename)

    create_pdf(
        output_path=output_path,
        name=name,
        rooted=rooted,
        heart=heart,
        expression=expression,
        mental=mental,
        awakened=awakened,
        life_path=life_path_text,
        destiny=destiny_text
    )

    # 6) Email the PDF
    try:
        send_email_with_attachment(
            to_email=email,
            subject="Your Soul Blueprint PDF",
            body=f"Hi {name},\n\nHere is your personalized Soul Blueprint. May it guide you gently on your path.\n\nWith love,\nSoul Aligned",
            attachment_path=output_path
        )
    except Exception as e:
        print(f"Email failed: {e}")

    # 7) Confirmation page
    return render_template('confirmation.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
