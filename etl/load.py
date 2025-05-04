import psycopg2
from psycopg2 import DatabaseError
from pathlib import Path
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sql.config import GenerateConfig


class Loader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Loader, cls).__new__(cls)
            cls._instance.db_config = GenerateConfig.config()
        return cls._instance

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()

    def initialize_tables(self):
        sql_path = Path(__file__).resolve().parent.parent / "sql" / "create_schema.sql"
        with sql_path.open("r") as file:
            query = file.read()
        try:
            self.cursor.execute(query)
        except DatabaseError as e:
            raise e

    def insert_weather_data(self, weather_data):
        try:
            # Make sure date column is in the correct format for db
            df_copy = weather_data.copy()
            if not pd.api.types.is_datetime64_any_dtype(df_copy["date"]):
                df_copy["date"] = pd.to_datetime(df_copy["date"])

            # Fill any NA values with appropriate defaults
            df_copy = df_copy.fillna(
                {
                    "temperature": 0.0,
                    "feels_like": 0.0,
                    "humidity": 0.0,
                    "precipitation": 0.0,
                    "wind_speed": 0.0,
                }
            )

            for _, row in df_copy.iterrows():
                self.cursor.execute(
                    """
                    INSERT INTO weather_data 
                    (date, temperature, feels_like, humidity, precipitation, wind_speed)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        row["date"],
                        float(row["temperature"]),
                        float(row["feels_like"]),
                        float(row["humidity"]),
                        float(row["precipitation"]),
                        float(row["wind_speed"]),
                    ),
                )
        except DatabaseError as e:
            self.conn.rollback()
            raise DatabaseError(f"Error inserting weather data: {e}")
