from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates


def plot_series(time,
                series,
                value=None,
                title=None):

    if value is None:
        value = series.name.title()
    if title is None:
        title = f"{time.name.title()} VS. {value}: Tiktok Data"
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time, series,color="purple", alpha=0.5)

    ax.set_title(title)
    ax.set_ylabel(value)
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    ax.xaxis.set_major_formatter(DateFormatter("%m-%d"))

    plt.grid(True)
    plt.show()

    plt.show()