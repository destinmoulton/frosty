import requests

import config


def get_weather_data():
    '''Get the weather forecast from the API
    '''

    params = {
        "id": config.api["location_id"],
        "units": config.api["units"],
        "appid": config.api["key"]
    }

    res = requests.get(api["url"], params=params)

    if res.status_code == 200:
        return res.json()

    return {}
