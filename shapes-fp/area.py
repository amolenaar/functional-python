import math

from shapes import ShapeType


def area(shape):
    shape_type, *args = shape
    if shape_type == ShapeType.CIRCLE:
        (radius,) = args
        return math.pi * radius * radius
    elif shape_type == ShapeType.SQUARE:
        (side,) = args
        return side * side
    else:
        raise TypeError(f"Unknown shape: {shape}")


# NB. This would make a nice candidate for Structural Pattern Matching
#     https://www.python.org/dev/peps/pep-0622.
#
# def area__Python_3_10(shape):
#     match shape:
#         case (ShapeType.CIRCLE, radius):
#             return math.pi * radius * radius
#         case (ShapeType.SQUARE, side):
#             return side * side
#         case _:
#             raise TypeError(f"Unknown shape: {shape}")
