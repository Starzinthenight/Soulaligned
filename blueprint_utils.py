import ephem
from datetime import datetime

def get_astrology_data(name, birthdate, birthtime, birthplace, latitude, longitude):
    try:
        birth_datetime = datetime.strptime(f"{birthdate} {birthtime}", "%Y-%m-%d %H:%M")
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = birth_datetime

        sun = ephem.Sun(observer)
        moon = ephem.Moon(observer)
        mars = ephem.Mars(observer)
        mercury = ephem.Mercury(observer)
        neptune = ephem.Neptune(observer)

        ascendant_deg = (observer.sidereal_time() * 15) % 360

        return {
            "Sun": sun.ra,
            "Moon": moon.ra,
            "Mars": mars.ra,
            "Mercury": mercury.ra,
            "Neptune": neptune.ra,
            "Ascendant": ascendant_deg
        }
    except Exception as e:
        return {"error": str(e)}

def calculate_life_path(birthdate):
    digits = [int(char) for char in birthdate if char.isdigit()]
    total = sum(digits)
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

def get_blueprint_keys(astro_data, name, birthdate):
    life_path = calculate_life_path(birthdate)
    modules = [
        "Rooted Foundation",
        "Self Expression",
        "Heart of Connection",
        "Mental Mastery",
        "Awakened Self"
    ]
    return {
        "Life Path Number": life_path,
        "Destiny Number": life_path,
        "Unlocked Modules": modules,
        "Soul Summary": f"{name}, your life path is {life_path}. You are ready to align with your Soul Blueprint."
    }