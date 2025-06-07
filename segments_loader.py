import json

def load_segments():
    with open("segments.json", "r", encoding="utf-8") as file:
        return json.load(file)
