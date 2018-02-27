from datetime import datetime, timedelta

import config


def get_min_temp_and_time(forecast_data, start_datetime, end_datetime):
    '''Get the minimum temperature and time within a datetime range.

    Parameters
    ----------
    forecast_data : list
        List of dicts containing the future weather data.
    start_datetime : datetime
        The initial time to start testing temps
    end_datetime : datetime
        The time to stop testing temps

    Returns
    -------
    tuple
        Minimum temp, Time min temp occurred

    '''
    min_temp = 100
    min_time = {}
    for fcast in forecast_data:
        dt = datetime.fromtimestamp(fcast['dt'], config.zones["orig"])
        forecast_time = dt.astimezone(config.zones["local"])

        if start_datetime < forecast_time < end_datetime:
            if fcast["main"]["temp_min"] < min_temp:
                min_temp = fcast["main"]["temp_min"]
                min_time = forecast_time

    return (min_temp, min_time)
