from etl.extract import Extractor
from etl.transform import Transformer
from etl.load import Loader

ex = Extractor()
ts = Transformer()
ld = Loader()

# weather_data = ex.api_request_creator()
# ts.transform_json_to_df(weather_data)
ld.initialize_tables()
