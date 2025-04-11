# extract.py

import requests
import config

def extract_data():
    """
    Extract earthquake data from USGS API.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/application.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
        print("Data successfully extracted from the API.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error extracting data: {e}")
        return None