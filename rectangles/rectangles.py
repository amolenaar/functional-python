"""Playing around with rectangles.

Rules: 
* You're not allows to use `for` and `while` loops
* You're not allowed to reassign variables
"""

from functools import reduce
from pprint import pprint
from typing import NamedTuple


class Rectangle(NamedTuple):
    x: int
    y: int
    w: int  # > 0
    h: int  # > 0


RECTANGLES = [
    Rectangle(0, 0, 1, 4),
    Rectangle(1, -1, 2, 2),
    Rectangle(0, 2, 2, 2),
    Rectangle(5, 5, 5, 5),
    Rectangle(1, 3, 2, 3),
    Rectangle(6, 3, 3, 2),
]


# TODO: Find all rectangles with an area > 5


def rectangles_with_an_area_gt_5(rectangles):

    result = []
    for r in rectangles:
        if r.w * r.h > 5:
            result.append(r)

    return result


# TODO: Find the smallest rectangle that contains all rectangles


def find_the_smallest_rectangle_that_contains_all_rectangles(rectangles):

    x0, y0, x1, y1 = rectangles[0]
    x1 = x0 + x1
    y1 = y0 + y1

    for r in rectangles[1:]:
        if r.x < x0:
            x0 = r.x
        if r.y < y0:
            y0 = r.y
        if r.x + r.w > x1:
            x1 = r.x + r.w
        if r.y + r.h > y1:
            y1 = r.y + r.h

    return Rectangle(x0, y0, x1 - x0, y1 - y0)


# TODO: Find all rectangles that intersect with point (0, 0)

# TODO: Find all clusters of overlapping rectangles
