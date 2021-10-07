from enum import Enum


class ShapeType(Enum):
    CIRCLE = 1
    SQUARE = 2


def circle(radius):
    return (ShapeType.CIRCLE, radius)


def square(side):
    return (ShapeType.SQUARE, side)
