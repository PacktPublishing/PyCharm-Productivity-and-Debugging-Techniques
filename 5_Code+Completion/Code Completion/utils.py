from matplotlib import pyplot as plt

from point import Point


def draw(x, y):
    # set up range of the plot
    limit = max(x, y) + 1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    # lines corresponding to x- and y-coordinates
    plt.plot([x, x], [0, y], '-', c='blue', linewidth=3)
    plt.plot([0, x], [y, y], '-', c='blue', linewidth=3)

    plt.scatter(x, y, s=100, marker='o', c='red')  # actual point

    ax.set_xlim((-limit, limit))
    ax.set_ylim((-limit, limit))

    # axis arrows
    left, right = ax.get_xlim()
    bottom, top = ax.get_ylim()
    Point.draw_arrow(bottom, left, right, top)

    plt.grid()
    plt.show()