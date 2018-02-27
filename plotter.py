from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib import dates
from pprint import pprint

import config


def plot_temperature_graph(data, start_datetime, cutoff_datetime):
    x_axis = ["empty"]
    y_axis = []
    for fcast in data["list"]:
        dt = datetime.fromtimestamp(fcast['dt'], config.zones["orig"])
        forecast_time = dt.astimezone(config.zones["local"])

        if start_datetime < forecast_time < cutoff_datetime:
            y_axis.append(fcast["main"]["temp_min"])
            x_axis.append(forecast_time.strftime("%-I:%M %p"))

    fig, axes = plt.subplots(1, 1, figsize=(6, 5), dpi=100)

    plt.title(start_datetime.strftime("%A %b %-d %-I:%M %p") +
              " to " + cutoff_datetime.strftime("%A %b %-d %-I:%M %p"))

    plt.ylabel("Degrees F")
    axes.plot(y_axis, c="red", linestyle="None", marker="o")
    axes.set_xticklabels(x_axis, rotation=25)

    fig.savefig('temps_plot.png')
