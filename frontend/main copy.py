from flask import Flask, request, redirect, send_from_directory
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/success.html')
def success():
    return send_from_directory('frontend', 'success.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('fullName')
    email = request.form.get('email')
    birthdate = request.form.get('birthDate')
    birthtime = request.form.get('birthTime')
    birthplace = request.form.get('placeOfBirth')

    # Placeholder — we’ll hook this up to your real logic in blueprint_utils
    print("Form data received:", name, email, birthdate, birthtime, birthplace)

    return redirect('/success.html')

if __name__ == '__main__':
    app.run(debug=True)
