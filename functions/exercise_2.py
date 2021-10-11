#
# Exercise 2:
#
# We are interrested in the execution time of our functional code.
#
# Create a higher order function that will measure the time it takes to
# execute a function.
#
# BONUS: how are you going to test this function?
#

from functools import reduce
from operator import add
import time


def measure(f):
    """Measure execution time of a function.

    >>> measure(lambda: reduce(add, range(0, 1000)))
    (499500, 3.48e-05)

    Where `499500` is the result of the calculation and
    `3.48e-05` is the time it took to execute.
    """
