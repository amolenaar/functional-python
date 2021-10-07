import math

from shape import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius * self._radius
