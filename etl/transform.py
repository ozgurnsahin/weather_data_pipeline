import pandas as pd
import logging

logger = logging.getLogger(__name__)


class Transformer:
    def __init__(self):
        pass

    def transform_json_to_df(self, raw_data):
        try:
            df = pd.DataFrame.from_dict(raw_data["days"])

            # Select and rename columns as needed
            df = df[
                ["datetime", "temp", "feelslike", "humidity", "precip", "windspeed"]
            ]
            df.columns = [
                "date",
                "temperature",
                "feels_like",
                "humidity",
                "precipitation",
                "wind_speed",
            ]

            # Convert data types
            df["date"] = pd.to_datetime(df["date"])
            df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
            df["feels_like"] = pd.to_numeric(df["feels_like"], errors="coerce")
            df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")
            df["precipitation"] = pd.to_numeric(df["precipitation"], errors="coerce")
            df["wind_speed"] = pd.to_numeric(df["wind_speed"], errors="coerce")

            # Handle missing values
            df.ffill(inplace=True)  # Forward fill missing values
            df.dropna(inplace=True)  # Drop any remaining missing values

            logger.info("Weather data is transformed")
            return df
        except ValueError as err:
            logger.error(f"Data transformation is failed error:{err}")
