import config

params = {
    "id": config.api["location_id"],
    "units": config.api["units"],
    "appid": config.api["key"]
}

res = requests.get(api["url"], params=params)
print(res.url)

from_zone = tz.gettz('UTC')
this_zone = tz.gettz('America/Denver')

now = datetime.now()
current_day = now.date()
tomorrow = timedelta(days=1) + now
tomorrow_cutoff_time = datetime(
    tomorrow.year, tomorrow.month, tomorrow.day, 12, 0, 0, 0).replace(tzinfo=this_zone)


if res.status_code == 200:
    data = res.json()

    for fcast in data["list"]:
        dt = datetime.fromtimestamp(fcast['dt'], from_zone)
        forecast_time = dt.astimezone(this_zone)

        if forecast_time < tomorrow_cutoff_time:
            pprint(fcast["main"]["temp_min"])
