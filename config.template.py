from dateutil import tz

zones = {
    "orig": tz.gettz('UTC'),
    "local": tz.gettz('<YOUR_TIMEZONE>')
}

api = {
    "url": "http://api.openweathermap.org/data/2.5/forecast",
    "key": "<YOUR_KEY_HERE>",
    "location_id": "<YOUR_OPEN_WEATHER_MAP_LOCATION_ID>",
    "units": "imperial"
}

email = {
    "from": {
        "name": "Frosty",
        "email": "<FROM_EMAIL_ADDRESS_HERE>"
    },
    "to": {
        "name": "<RECIPIENT_NAME_HERE>",
        "email": "<RECIPIENT_EMAIL_ADDRESS>"
    },
    "smtp": {
        "host": "<SMTP_HOST>",
        "user": "<SMTP_USER>",
        "password": "<SMTP_PASS>",
        "port": 465,
        "ssl": True
    }
}

proxies = {
    "https": "<PROXY_URL_HERE>"
}
