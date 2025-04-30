import json
import requests

SEGMENTS_URL = 'https://gist.githubusercontent.com/Starzinthenight/d4178399c7f1c43972fcfc3fb53c6818/raw/4816e12595185d7db5116b89683e1e200155d281/segments.json'

def load_segments():
    """Download and return segments JSON from your Gist."""
    response = requests.get(SEGMENTS_URL)
    response.raise_for_status()
    return json.loads(response.text)
