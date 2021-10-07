import math

from circle import Circle
from square import Square


def test_circle_area():
    c = Circle(1)

    assert c.area() == math.pi


# def test_circle_circumference():
#     c = Circle(1)
#
#     assert c.circumference() == 2 * math.pi


def test_square_area():
    s = Square(2)

    assert s.area() == 4


# def test_square_circumference():
#     s = Square(2)
#
#     assert s.circumference() == 8
