import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import colormaps
import matplotlib
import warnings

from dumbbell.utils import _is_numerical


def lollipop(
    x,
    y,
    c=None,
    color=None,
    kind="vertical",
    v_start=0,
    h_start=0,
    labels=None,
    cmap=None,
    norm=None,
    ax=None,
    scatter_kwargs={},
    plot_kwargs={},
    labels_kwargs={},
) -> matplotlib.axes.Axes:
    """ """

    if len(x) != len(y):
        raise ValueError("x and y must be the same length.")

    if ax is None:
        ax = plt.gca()

    if c is not None:
        if norm is None:
            if not _is_numerical(c[0]):
                warnings.warn("c must contains numerical value.")
            else:
                norm = mcolors.Normalize(vmin=min(c), vmax=max(c))

    if not _is_numerical(x[0]):
        ax.set_xticks([])
    elif not _is_numerical(y[0]):
        ax.set_yticks([])

    for i in range(len(x)):
        x_value = x[i]
        y_value = y[i]

        if c is not None:
            if cmap is None:
                cmap = plt.get_cmap("viridis")
            elif isinstance(cmap, str):
                if cmap not in list(colormaps):
                    raise ValueError("Invalid cmap value.")
                else:
                    cmap = plt.get_cmap(cmap)
            color = cmap(norm(c[i]))
        else:
            if color is None:
                color = "#5778b1"

        if kind == "vertical":
            if not _is_numerical(x[0]):
                x_loc = i + 1
                if labels:
                    s = x_value
            else:
                x_loc = x_value
                s = y_value

            y_loc = y_value
            if labels:
                ax.text(
                    x=x_loc, y=y_loc, s=s, ha="center", va="center", **labels_kwargs
                )
            ax.plot([x_loc, x_loc], [v_start, y_loc], color=color, **plot_kwargs)

        elif kind == "horizontal":
            if not _is_numerical(y[0]):
                y_loc = i + 1
                if labels:
                    s = y_value
            else:
                y_loc = y_value
                s = x_value

            x_loc = x_value
            if labels:
                ax.text(
                    x=x_loc, y=y_loc, s=s, ha="center", va="center", **labels_kwargs
                )
            ax.plot([h_start, x_loc], [y_loc, y_loc], color=color, **plot_kwargs)

        else:
            raise ValueError(
                f"`kind` must be either 'vertical' or 'horizontal', not: {kind}"
            )

        ax.scatter(x_loc, y_value, color=color, **scatter_kwargs)

    return ax


if __name__ == "__main__":
    import string
    import numpy as np
    import pandas as pd

    np.random.seed(0)
    x = list(range(20))
    x = list(string.ascii_lowercase[:20])
    y = np.random.normal(size=20)
    df = pd.DataFrame({"x": x, "y": y})

    labels_kwargs = dict(color="red", size=12, weight="bold")
    kind = "horizontal"

    fig, ax = plt.subplots(figsize=(5, 6))
    lollipop(
        x=df["x"],
        y=df["y"],
        c=df["y"],
        labels=True,
        labels_kwargs=labels_kwargs,
        kind=kind,
    )
    plt.show()
