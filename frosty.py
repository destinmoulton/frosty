#!/usr/bin/python3

from api import get_weather_data
from datetimehelper import get_end_datetime, get_start_datetime
from emailer import send_email

from forecast import get_min_temp_and_time
from plotter import plot_forecast_chart


start_datetime = get_start_datetime()
end_datetime = get_end_datetime()

data = get_weather_data()
plot_forecast_chart(data["list"], start_datetime, end_datetime)
min_data = get_min_temp_and_time(data["list"], start_datetime, end_datetime)
send_email(min_data)
