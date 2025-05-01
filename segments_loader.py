import json
import requests

SEGMENTS_URL = 'https://gist.githubusercontent.com/Starzinthenight/d4178399c7f1c43972fcfc3fb53c6818/raw/ae0acb830ffa2f8f8e4806b72047e29a62e2802a/segments.json'

def load_segments():
    """Download and return segments JSON from your Gist."""
    response = requests.get(SEGMENTS_URL)
    response.raise_for_status()
    return json.loads(response.text)

