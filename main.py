import os
from flask import Flask, request, redirect
import blueprint_utils
import segments_loader
from urllib.parse import quote_plus

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    # 1) Read the form inputs
    name       = request.form.get('fullName', '').strip()
    email      = request.form.get('email', '').strip()
    birthdate  = request.form.get('birthDate', '')
    birthtime  = request.form.get('birthTime', '')
    birthplace = request.form.get('placeOfBirth', '').strip()

    # 2) Compute your report and pull segments
    report   = blueprint_utils.create_report(name, birthdate, birthtime, birthplace)
    segments = segments_loader.load_segments()

    # 3) Match them up
    rooted     = segments.get(f"mars_{report['chart']['mars_sign'].lower()}", "")
    heart      = segments.get(f"moon_{report['chart']['moon_sign'].lower()}", "")
    expression = segments.get(f"sun_{report['chart']['sun_sign'].lower()}", "")
    mental     = segments.get(f"mercury_{report['chart']['mercury_sign'].lower()}", "")
    awakened   = segments.get(f"ascendant_{report['chart']['ascendant_sign'].lower()}", "")
    life_path  = segments.get(f"life_path_{report['life_path']}", "")
    destiny    = segments.get(f"destiny_{report['destiny_number']}", "")

    # 4) Build the URL query string
    params = {
        'rooted': rooted,
        'heart': heart,
        'expression': expression,
        'mental': mental,
        'awakened': awakened,
        'life_path': life_path,
        'destiny': destiny
    }
    query = '&'.join(f"{key}={quote_plus(value)}" for key, value in params.items())

    # 5) Redirect straight to your Webador results page
    return redirect(f"https://www.soulaligned.life/soul-blueprint-roadmap?{query}")

if __name__ == '__main__':
    # Port binding for Render (or default 5000 locally)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
