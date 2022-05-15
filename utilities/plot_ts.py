import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

COLORS = ["purple", "red", "blue", "green", "black"]


def plot_series(time,
                *args,
                value=None,
                title=None,
                labels=None):
    fig, ax = plt.subplots(figsize=(10, 6))

    if labels is None:
        labels = range(len(args))

    for i, series in enumerate(args):
        ax.plot(time, series, color=COLORS[i], alpha=0.5, label=labels[i])
        fig.autofmt_xdate()

        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
        ax.xaxis.set_major_formatter(DateFormatter("%m-%d"))

    if value is None and args[0].name:
        value = args[0].name.title()
    if title is None and args[0].name and time.name:
        title = f"{time.name.title()} VS. {value}: Tiktok Data"

    ax.set_title(title)
    ax.set_ylabel(value)

    plt.grid(True)

    if len(args) > 1:
        plt.legend()
    plt.show()

    plt.show()