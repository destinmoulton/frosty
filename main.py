

from api import get_weather_data
from emailer import send_email
from forecast import get_minimum_temperature

data = get_weather_data()
min_data = get_minimum_temperature(data)
send_email(min_data)
