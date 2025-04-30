from datetime import datetime
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

def reduce_number(n):
    """Reduce a number to a single digit unless it is a master number (11, 22, 33)."""
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(digit) for digit in str(n))
    return n

def calculate_life_path(birthdate_str):
    """Calculate Life Path Number from birthdate."""
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    total = birthdate.day + birthdate.month + birthdate.year
    return reduce_number(total)

def calculate_destiny_number(name):
    """Calculate Destiny Number from full name."""
    letter_values = {
        'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
        'J':1,'K':2,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,
        'S':1,'T':2,'U':3,'V':4,'W':5,'X':6,'Y':7,'Z':8
    }
    name = name.upper()
    total = sum(letter_values.get(c, 0) for c in name if c.isalpha())
    return reduce_number(total)

def create_report(name, birthdate, birthtime, birthplace):
    """Main function to generate the Soul Blueprint data."""

    # Numerology part
    life_path = calculate_life_path(birthdate)
    destiny = calculate_destiny_number(name)

    # Astrology calculation
    date_parts = birthdate.split('-')
    time_parts = birthtime.split(':')

    date_str = f"{date_parts[0]}/{date_parts[1]}/{date_parts[2]}"
    time_str = f"{time_parts[0]}:{time_parts[1]}:00"

    # Placeholder GeoPos (London for now)
    pos = GeoPos(51.5074, -0.1278)  # London coordinates as floats

    dt = Datetime(date_str, time_str, '+00:00')  # Using UTC timezone for now
    chart = Chart(dt, pos)

    sun_sign = chart.get(const.SUN).sign
    moon_sign = chart.get(const.MOON).sign
    mercury_sign = chart.get(const.MERCURY).sign
    mars_sign = chart.get(const.MARS).sign
    ascendant_sign = chart.get(const.ASC).sign

    chart_data = {
        "sun_sign": sun_sign,
        "moon_sign": moon_sign,
        "mercury_sign": mercury_sign,
        "mars_sign": mars_sign,
        "ascendant_sign": ascendant_sign
    }

    # Print everything for confirmation
    print("Life Path:", life_path)
    print("Destiny Number:", destiny)
    print("Sun Sign:", sun_sign)
    print("Moon Sign:", moon_sign)
    print("Mercury Sign:", mercury_sign)
    print("Mars Sign:", mars_sign)
    print("Ascendant Sign:", ascendant_sign)

    report = {
        "name": name,
        "birthdate": birthdate,
        "birthtime": birthtime,
        "birthplace": birthplace,
        "life_path": life_path,
        "destiny_number": destiny,
        "chart": chart_data
    }

    return report
