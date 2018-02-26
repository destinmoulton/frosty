from datetime import datetime, timedelta
from pprint import pprint

import config


def get_minimum_temperature(data):

    now = datetime.now()
    current_day = now.date()
    tomorrow = timedelta(days=1) + now
    tomorrow_cutoff_time = datetime(
        tomorrow.year, tomorrow.month, tomorrow.day, 12, 0, 0, 0).replace(tzinfo=config.zones["local"])

    min_temp = 100
    min_time = {}
    for fcast in data["list"]:
        dt = datetime.fromtimestamp(fcast['dt'], config.zones["orig"])
        forecast_time = dt.astimezone(config.zones["local"])

        if forecast_time < tomorrow_cutoff_time:
            if fcast["main"]["temp_min"] < min_temp:
                min_temp = fcast["main"]["temp_min"]
                min_time = forecast_time

    return (min_temp, min_time)
