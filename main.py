import pyowm
import requests
from datetime import datetime
from dateutil import tz
from pprint import pprint

import config

params = {
    "id": config.api_location_id,
    "units": config.api_units,
    "appid": config.api_key
}

api_url = "http://api.openweathermap.org/data/2.5/forecast"

res = requests.get(api_url, params=params)
print(res.url)

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
if res.status_code == 200:
    data = res.json()

    for fcast in data["list"]:
        pprint(fcast)
