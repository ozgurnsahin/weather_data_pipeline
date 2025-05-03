from etl.extract import Extractor
from etl.transform import Transformer

ex = Extractor()
ts = Transformer()

weather_data = ex.api_request_creator()
