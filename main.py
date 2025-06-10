import os
from flask import Flask, request, jsonify, send_file
from generate_pdf import create_pdf
from blueprint_utils import get_blueprint_data
from segments import segments
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return "Soul Blueprint Generator is live!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    name = data.get("name", "Friend")

    # Get astrology, numerology, and HD data
    report = get_blueprint_data(data)

    # 1) Blueprint segments
    rooted = report.get("rooted_foundation", "")
    heart = report.get("heart_connection", "")
    expression = report.get("self_expression", "")
    mental = report.get("mental_mastery", "")
    awakened = report.get("awakened_self", "")

    # 2) Numerology segments
    lp = str(report['life_path'])
    dn = str(report['destiny_number'])

    # 3) Confirming number inside content
    lp_text = segments.get("lifePath", {}).get(lp, "")
    dn_text = segments.get("destiny", {}).get(dn, "")

    life_path_text = f"Your Life Path Number is {lp}.\n\n{lp_text}"
    destiny_text = f"Your Destiny Number is {dn}.\n\n{dn_text}"

    # 4) Generate PDF
    output_path = f"output/{name}_blueprint.pdf"
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

    return send_file(output_path, as_attachment=True)import os
from flask import Flask, request, jsonify, send_file
from generate_pdf import create_pdf
from blueprint_utils import get_blueprint_data
from segments import segments
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return "Soul Blueprint Generator is live!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    name = data.get("name", "Friend")

    # Get astrology, numerology, and HD data
    report = get_blueprint_data(data)

    # 1) Blueprint segments
    rooted = report.get("rooted_foundation", "")
    heart = report.get("heart_connection", "")
    expression = report.get("self_expression", "")
    mental = report.get("mental_mastery", "")
    awakened = report.get("awakened_self", "")

    # 2) Numerology segments
    lp = str(report['life_path'])
    dn = str(report['destiny_number'])

    # 3) Confirming number inside content
    lp_text = segments.get("lifePath", {}).get(lp, "")
    dn_text = segments.get("destiny", {}).get(dn, "")

    life_path_text = f"Your Life Path Number is {lp}.\n\n{lp_text}"
    destiny_text = f"Your Destiny Number is {dn}.\n\n{dn_text}"

    # 4) Generate PDF
    output_path = f"output/{name}_blueprint.pdf"
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

    return send_file(output_path, as_attachment=True)
