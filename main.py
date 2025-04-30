import os
from flask import Flask, request, render_template
import blueprint_utils
import segments_loader

# Tell Flask where to find your templates
app = Flask(__name__, template_folder='templates')

@app.route('/generate', methods=['POST'])
def generate():
    name       = request.form.get('fullName', '').strip()
    email      = request.form.get('email', '').strip()
    birthdate  = request.form.get('birthDate', '')
    birthtime  = request.form.get('birthTime', '')
    birthplace = request.form.get('placeOfBirth', '').strip()

    report   = blueprint_utils.create_report(name, birthdate, birthtime, birthplace)
    segments = segments_loader.load_segments()

    rooted     = segments.get(f"mars_{report['chart']['mars_sign'].lower()}", "")
    heart      = segments.get(f"moon_{report['chart']['moon_sign'].lower()}", "")
    expression = segments.get(f"sun_{report['chart']['sun_sign'].lower()}", "")
    mental     = segments.get(f"mercury_{report['chart']['mercury_sign'].lower()}", "")
    awakened   = segments.get(f"ascendant_{report['chart']['ascendant_sign'].lower()}", "")
    life_path  = segments.get(f"life_path_{report['life_path']}", "")
    destiny    = segments.get(f"destiny_{report['destiny_number']}", "")

    # Render the Jinja2 template with all six sections
    return render_template(
        'results.html',
        rooted=rooted,
        heart=heart,
        expression=expression,
        mental=mental,
        awakened=awakened,
        life_path=life_path,
        destiny=destiny
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
