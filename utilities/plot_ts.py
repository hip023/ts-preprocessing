from matplotlib import pyplot as plt


def plot_series(time,
                series,
                value="Value",
                title=""):
    plt.figure(figsize=(10, 6))
    plt.plot(time, series,color="purple", alpha=0.5)
    plt.title(title)
    plt.ylabel(value)
    plt.grid(True)
    plt.show()