import matplotlib.pyplot as plt
import matplotlib as mpl


def lollipop(
    x,
    y,
    c=None,
    color=None,
    cmap=None,
    kind="vertical",
    v_start=0,
    h_start=0,
    ax=None,
    scatter_kwargs={},
    plot_kwargs={},
) -> None:
    """ """

    if ax is None:
        ax = plt.gca()

    if c is not None:
        norm = mpl.colors.Normalize(vmin=min(c), vmax=max(c))

    for i, (x_value, y_value) in enumerate(zip(x, y)):
        if c is not None:
            if cmap is None:
                cmap = plt.get_cmap("viridis_r")
            color = cmap(norm(c[i]))
        else:
            if color is None:
                color = "#5778b1"

        if kind == "vertical":
            ax.scatter(x_value, y_value, color=color, **scatter_kwargs)
            ax.plot([x_value, x_value], [v_start, y_value], color=color, **plot_kwargs)
        elif kind == "horizontal":
            ax.scatter(x_value, y_value, color=color, **scatter_kwargs)
            ax.plot([h_start, x_value], [y_value, y_value], color=color, **plot_kwargs)
        else:
            raise ValueError(
                f"`kind` must be either 'vertical' or 'horizontal', not: {kind}"
            )


if __name__ == "__main__":
    y = [1, 2, 3, 4, 5]
    x = [10, 50, 27, 48, 1]
    fig, ax = plt.subplots()
    lollipop(x=x, y=y, c=y, kind="horizontal")
    plt.show()
