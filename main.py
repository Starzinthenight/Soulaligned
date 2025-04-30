import os
from flask import Flask, request, render_template
import blueprint_utils
import segments_loader

app = Flask(__name__, template_folder='templates')

@app.route('/generate', methods=['POST'])
def generate():
    # 1) Read form inputs
    name       = request.form.get('fullName','').strip()
    birthdate  = request.form.get('birthDate','')
    birthtime  = request.form.get('birthTime','')
    birthplace = request.form.get('placeOfBirth','').strip()

    # 2) Compute chart + load segments
    report   = blueprint_utils.create_report(name, birthdate, birthtime, birthplace)
    segments = segments_loader.load_segments()

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

    # 4) Life Path & Destiny with numeric fallback
    lp = report['life_path']
    dn = report['destiny_number']
    life_path_text = segments.get(f"life_path_{lp}",
                                  f"Your Life Path Number is {lp}.")
    destiny_text   = segments.get(f"destiny_{dn}",
                                  f"Your Destiny Number is {dn}.")

    # 5) Render the template
    return render_template('results.html',
                           rooted=rooted,
                           heart=heart,
                           expression=expression,
                           mental=mental,
                           awakened=awakened,
                           life_path=life_path_text,
                           destiny=destiny_text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
