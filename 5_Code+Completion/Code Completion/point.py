from math import sqrt


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point {self.x}, {self.y}'

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def distance(self, p):
        diff = self - p
        return sqrt(diff.x ** 2 + diff.y ** 2)
