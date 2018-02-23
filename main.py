import pyowm
import requests

import config

params = {
    "id": config.api_location_id,
    "units": config.api_units,
    "appid": config.api_key
}

api_url = "http://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_url, params=params)
print(response.content)
# if response.status_code == "200":
