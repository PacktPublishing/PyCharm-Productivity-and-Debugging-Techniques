from math import sqrt

from matplotlib import pyplot as plt

from utils import draw


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point {self.x}, {self.y}'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance(self, other):
        diff = self - other
        distance = sqrt(diff.x ** 2 + diff.y ** 2)
        return distance

    @staticmethod
    def draw_arrow(bottom, left, right, top):
        plt.arrow(left, 0, right - left, 0, length_includes_head=True,
                  head_width=0.15)
        plt.arrow(0, bottom, 0, top - bottom,
                  length_includes_head=True,
                  head_width=0.15)


if __name__ == '__main__':
    p1 = Point(1, 0)
    p2 = Point(5, 3)

    draw(p2.x, p2.y)