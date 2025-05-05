from etl.extract import Extractor
from etl.transform import Transformer
from etl.load import Loader
import argparse

ex = Extractor()
ts = Transformer()
ld = Loader()


def main():
    parser = argparse.ArgumentParser(
        description="Database to Google Sheets Sync"
    )  # python main.py default start
    parser.add_argument(
        "--now", action="store_true", help="Perform immediate sync"
    )  # python main.py --now manual immediate start

    args = parser.parse_args()

    if args.now:
        weather_data = ex.api_request_creator()
        transformed_data = ts.transform_json_to_df(weather_data)
        ld.insert_weather_data(transformed_data)


if __name__ == "__main__":
    main()
