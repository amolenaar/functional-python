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


# Find all rectangles with an area > 5

# Find the smallest rectangle that contains all rectangles

# Find all rectangles that intersect with point (0, 0)

# Find all clusters of overlapping rectangles
