import math

from shapes import circle, square
from area import area


def test_circle_area():
    c = circle(1)

    assert area(c) == math.pi


def test_square_area():
    s = square(2)

    assert area(s) == 4


# def test_circle_circumference():
#     c = circle(1)
#
#     assert circumference(c) == 2 * math.pi


# def test_square_circumference():
#     s = square(2)
#
#     assert circumference(s) == 4 * 2
