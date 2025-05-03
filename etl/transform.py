import pandas as pd
import json


class Transformer:
    def __init__(self):
        pass

    def transform_json_to_df(self, raw_data):
        try:
            df = pd.DataFrame.from_dict(raw_data)
            print(df.head())
        except ValueError as err:
            print(err)
