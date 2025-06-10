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

    # 3) Retrieve blueprint descriptions (astrological)
    chart = report['chart']
    rooted     = segments.get(f"mars_{chart['mars_sign'].lower()}", f"Mars in {chart['mars_sign']}")
    heart      = segments.get(f"moon_{chart['moon_sign'].lower()}", f"Moon in {chart['moon_sign']}")
    expression = segments.get(f"sun_{chart['sun_sign'].lower()}", f"Sun in {chart['sun_sign']}")
    mental     = segments.get(f"mercury_{chart['mercury_sign'].lower()}", f"Mercury in {chart['mercury_sign']}")
    awakened   = segments.get(f"ascendant_{chart['ascendant_sign'].lower()}", f"Ascendant in {chart['ascendant_sign']}")

    # 4) Numerology segments (nested dictionary lookup)
    lp = str(report['life_path'])
    dn = str(report['destiny_number'])

    life_path_text = segments.get("lifePath", {}).get(lp, f"Your Life Path Number is {lp}.")
    destiny_text   = segments.get("destiny", {}).get(dn, f"Your Destiny Number is {dn}.")

    # 5) Generate the PDF
    pdf_filename = f"soul_blueprint_{uuid.uuid4().hex}.pdf"
    output_dir = "output"
    output_path = os.path.join(output_dir, pdf_filename)
    os.makedirs(output_dir, exist_ok=True)

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
            body=f"Hi {name},\n\nHere is your personalised Soul Blueprint. May it guide you gently on your path.\n\nWith love,\nSoul Aligned",
            attachment_path=output_path
        )
    except Exception as e:
        print(f"[Email Error] Could not send to {email}: {e}")

    # 7) Show confirmation page
    return render_template('confirmation.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
