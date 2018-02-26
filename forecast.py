from datetime import datetime, timedelta
from pprint import pprint

import config


def get_minimum_temperature(data, start_datetime, cutoff_datetime):
    min_temp = 100
    min_time = {}
    for fcast in data["list"]:
        dt = datetime.fromtimestamp(fcast['dt'], config.zones["orig"])
        forecast_time = dt.astimezone(config.zones["local"])

        if start_datetime < forecast_time < cutoff_datetime:
            if fcast["main"]["temp_min"] < min_temp:
                min_temp = fcast["main"]["temp_min"]
                min_time = forecast_time

    return (min_temp, min_time)
