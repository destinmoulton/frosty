from datetime import datetime, timedelta

import config


def get_start_datetime():
    now = datetime.now()
    return datetime(
        now.year, now.month, now.day, 12, 0, 0, 0).replace(tzinfo=config.zones["local"])


def get_cutoff_datetime():
    now = datetime.now()
    tomorrow = timedelta(days=1) + now
    return datetime(
        tomorrow.year, tomorrow.month, tomorrow.day, 12, 0, 0, 0).replace(tzinfo=config.zones["local"])
