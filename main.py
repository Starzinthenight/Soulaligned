from flask import Flask, request, redirect, send_from_directory
import blueprint_utils
import segments_loader  # <-- New import to load your segments

app = Flask(__name__, static_folder='frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/success.html')
def success():
    return send_from_directory('frontend', 'success.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    name = data['fullName']
    email = data['email']
    birthdate = data['birthDate']
    birthtime = data['birthTime']
    birthplace = data['placeOfBirth']

    print("Form data received:", name, email, birthdate, birthtime, birthplace)

    # Call your real numerology + astrology function
    report = blueprint_utils.create_report(name, birthdate, birthtime, birthplace)

    # Load your Soul Blueprint segments from your gist
    segments = segments_loader.load_segments()

    # Match report results to correct writing pieces
    rooted = segments.get(f"mars_{report['chart']['mars_sign'].lower()}", "Rooted: Missing")
    heart = segments.get(f"moon_{report['chart']['moon_sign'].lower()}", "Heart: Missing")
    expression = segments.get(f"sun_{report['chart']['sun_sign'].lower()}", "Expression: Missing")
    mental = segments.get(f"mercury_{report['chart']['mercury_sign'].lower()}", "Mental: Missing")
    awakened = segments.get(f"ascendant_{report['chart']['ascendant_sign'].lower()}", "Awakened: Missing")
    life_path = segments.get(f"life_path_{report['life_path']}", "Life Path: Missing")
    destiny_number = segments.get(f"destiny_{report['destiny_number']}", "Destiny: Missing")

    # Print personalized Soul Blueprint
    print("\n🔮 Your Soul Blueprint 🔮")
    print("\nRooted Foundation:\n", rooted)
    print("\nHeart of Connection:\n", heart)
    print("\nSelf Expression:\n", expression)
    print("\nMental Mastery:\n", mental)
    print("\nAwakened Self:\n", awakened)
    print("\nLife Path Number:\n", life_path)
    print("\nDestiny Number:\n", destiny_number)

    return redirect('/success.html')

if __name__ == '__main__':
    app.run(debug=True)
