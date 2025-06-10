import os
from flask import Flask, request, send_file, render_template
from dotenv import load_dotenv
from generate_pdf import create_pdf
from blueprint_utils import get_astrology_data, get_life_path_number, get_destiny_number
import json

load_dotenv()
app = Flask(__name__)

# Load personality segments
with open("data/personality_segments.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    email = request.form["email"]
    birth_date = request.form["birthdate"]
    birth_time = request.form["birthtime"]
    birth_place = request.form["birthplace"]

    # 1) Get astrology placements
    astro_data = get_astrology_data(birth_date, birth_time, birth_place)

    # 2) Get numerology
    life_path = get_life_path_number(birth_date)
    destiny_number = get_destiny_number(name)

    # 3) Get full label for each section (text only)
    report = {
        "name": name,
        "life_path": life_path,
        "destiny_number": destiny_number,
        "sun": astro_data["Sun"],
        "moon": astro_data["Moon"],
        "mercury": astro_data["Mercury"],
        "mars": astro_data["Mars"],
        "neptune": astro_data["Neptune"],
        "ascendant": astro_data["Ascendant"]
    }

    # 4) Numerology segments (nested dictionary lookup)
    lp = str(report['life_path'])
    dn = str(report['destiny_number'])

    life_path_msg = f"Your Life Path Number is {lp}.\n\n" + segments.get("lifePath", {}).get(lp, "")
    destiny_msg = f"Your Destiny Number is {dn}.\n\n" + segments.get("destiny", {}).get(dn, "")

    # 5) Blueprint segments
    rooted = segments["rooted"].get(report["mars"], "")
    heart = segments["heart"].get(report["moon"], "")
    expression = segments["expression"].get(report["sun"], "")
    mental = segments["mental"].get(report["mercury"], "")
    awakened = segments["awakened"].get(report["ascendant"], "")

    # 6) Create PDF and serve
    output_path = f"output/{name.replace(' ', '_')}_soulblueprint.pdf"
    create_pdf(
        output_path=output_path,
        name=name,
        rooted=rooted,
        heart=heart,
        expression=expression,
        mental=mental,
        awakened=awakened,
        life_path=life_path_msg,
        destiny=destiny_msg
    )

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
