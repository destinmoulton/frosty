

from api import get_weather_data
from datetimehelper import get_cutoff_datetime, get_start_datetime
from emailer import send_email

from forecast import get_minimum_temperature
from plotter import plot_temperature_graph


start_datetime = get_start_datetime()
cutoff_datetime = get_cutoff_datetime()

data = get_weather_data()
plot_temperature_graph(data, start_datetime, cutoff_datetime)
min_data = get_minimum_temperature(data, start_datetime, cutoff_datetime)
send_email(min_data)
