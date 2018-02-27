from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib import dates
from pprint import pprint

import config


def plot_forecast_chart(forecast_data, start_datetime, end_datetime):
    '''Plot the temperature forecast on a dot chart

    Parameters
    ----------
    forecast_data : list
        The list of API forecast data
    start_datetime : datetime
        The time to start analyzing forecast data
    end_datetime : datetime
        The time to end analyzing the forecast data
    '''
    x_axis = ["empty"]
    y_axis = []
    for fcast in forecast_data:
        dt = datetime.fromtimestamp(fcast['dt'], config.zones["orig"])
        forecast_time = dt.astimezone(config.zones["local"])

        if start_datetime < forecast_time < end_datetime:
            y_axis.append(fcast["main"]["temp_min"])
            x_axis.append(forecast_time.strftime("%-I:%M %p"))

    fig, axes = plt.subplots(1, 1, figsize=(6, 5), dpi=100)

    plt.title(start_datetime.strftime("%A %b %-d %-I:%M %p") +
              " to " + end_datetime.strftime("%A %b %-d %-I:%M %p"))

    plt.ylabel("Degrees F")
    axes.plot(y_axis, c="red", linestyle="None", marker="o")
    axes.set_xticklabels(x_axis, rotation=25)

    fig.savefig('temps_plot.png')
