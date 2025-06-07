import os
from flask import Flask, request, render_template
import blueprint_utils
import segments_loader
from generate_pdf import create_pdf  # Make sure this exists
from email_utils import send_email_with_attachment  # Uses Gmail SMTP
from dotenv import load_dotenv
import uuid

# Load .env credentials
load_dotenv()

app = Flask(__name__, template_folder='templates')

@app.route('/generate', methods=['POST'])
def generate():
    # 1) Read form inputs
    name       = request.form.get('fullName','').strip()
    email      = request.form.get('email','').strip()  # Added!
    birthdate  = request.form.get('birthDate','')
    birthtime  = request.form.get('birthTime','')
    birthplace = request.form.get('placeOfBirth','').strip()

    # 2) Compute chart + load segments
    report   = blueprint_utils.create_report(name, birthdate, birthtime, birthplace)
    segments = segments_loader.load_segments()
    for key, value in segments.items():
    if "✨" in value:
        print(f"Emoji found in: {key}")

    # 3) Lookup each area with fallback to the raw sign name
    rooted     = segments.get(f"mars_{report['chart']['mars_sign'].lower()}",
                              f"Mars in {report['chart']['mars_sign']}")
    heart      = segments.get(f"moon_{report['chart']['moon_sign'].lower()}",
                              f"Moon in {report['chart']['moon_sign']}")
    expression = segments.get(f"sun_{report['chart']['sun_sign'].lower()}",
                              f"Sun in {report['chart']['sun_sign']}")
    mental     = segments.get(f"mercury_{report['chart']['mercury_sign'].lower()}",
                              f"Mercury in {report['chart']['mercury_sign']}")
    awakened   = segments.get(f"ascendant_{report['chart']['ascendant_sign'].lower()}",
                              f"Ascendant in {report['chart']['ascendant_sign']}")

    # 4) Life Path & Destiny
    lp = report['life_path']
    dn = report['destiny_number']
    life_path_text = segments.get(f"life_path_{lp}", f"Your Life Path Number is {lp}.")
    destiny_text   = segments.get(f"destiny_{dn}", f"Your Destiny Number is {dn}.")

    # 5) Create the PDF
    pdf_filename = f"soul_blueprint_{uuid.uuid4().hex}.pdf"
    output_path = os.path.join("output", pdf_filename)

    create_pdf(
        output_path,
        name=name,
        rooted=rooted,
        heart=heart,
        expression=expression,
        mental=mental,
        awakened=awakened,
        life_path=life_path_text,
        destiny=destiny_text
    )

    # 6) Send the PDF via email
    try:
        send_email_with_attachment(
            to_email=email,
            subject="Your Soul Blueprint PDF ✨",
            body=f"Hi {name},\n\nHere is your personalized Soul Blueprint. May it guide you gently on your path.\n\nWith love,\nSoul Aligned",
            attachment_path=output_path
        )
    except Exception as e:
        print(f"Email failed: {e}")

    # 7) Render confirmation page (optional)
    return render_template('confirmation.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
