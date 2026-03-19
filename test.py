import requests
import json
from logger import logger

# Test the create_geo_loc endpoint
url = "http://127.0.0.1:8000/geo-loc/"

payload = {
    "latitude": 14.5994,
    "longitude": 120.9842,
    "address": {
        "street": "J.P. Laurel Street",
        "city": "Manila",
        "country": "Philippines",
        "landmark": "Malacañan Palace"
    }
}

try:
    response = requests.post(url, json=payload)
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    logger.error(f"Error: {e}")