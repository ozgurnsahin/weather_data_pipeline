from dotenv import load_dotenv
import logging
import requests
import os
import sys


load_dotenv()
logger = logging.getLogger(__name__)


class Extractor:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.lat = 41.015137
        self.lon = 28.979530
        self.exclude = "minutely,current,daily,alerts"
        self.url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={self.api_key}"

    def api_request_creator(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()

            logger.info("Fetching weather data")
            return data

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            sys.exit(1)
