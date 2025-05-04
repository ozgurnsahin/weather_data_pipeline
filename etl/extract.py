from dotenv import load_dotenv
import logging
import urllib.request
import json
import os
import sys


load_dotenv()
logger = logging.getLogger(__name__)


class Extractor:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Istanbul,TR?unitGroup=metric&include=current&key={self.api_key}&contentType=json"

    def api_request_creator(self):
        try:
            response = urllib.request.urlopen(self.url)

            json_data = json.load(response)

            logger.info("Fetching weather data")
            return json_data
        except urllib.request.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            sys.exit(1)
