"""Playing around with rectangles.

"""
from functools import reduce
from pprint import pprint
from typing import NamedTuple

from rectangles import (
    Rectangle,
    RECTANGLES,
    rectangles_with_an_area_gt_5,
    find_the_smallest_rectangle_that_contains_all_rectangles,
)


def test_find_all_shapes_with_an_area_gt_5():

    rectangles = rectangles_with_an_area_gt_5(RECTANGLES)

    assert rectangles == [
        Rectangle(x=5, y=5, w=5, h=5),
        Rectangle(x=1, y=3, w=2, h=3),
        Rectangle(x=6, y=3, w=3, h=2),
    ]


def test_find_the_smallest_rectangle_that_contains_all_rectangles():

    r = find_the_smallest_rectangle_that_contains_all_rectangles(RECTANGLES)

    assert r == Rectangle(0, -1, 10, 11)
