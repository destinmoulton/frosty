import pyowm
import requests
from datetime import datetime, timedelta
from dateutil import tz
from pprint import pprint

import config
from email import send_email
