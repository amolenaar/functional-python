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


def measure(func):
    """Measure execution time of a function.

    >>> measure(lambda: reduce(add, range(0, 1000)))
    (499500, 3.48e-05)

    Where `499500` is the result of the calculation and
    `3.48e-05` is the time it took to execute.
    """
    start_time = time.time()
    result = func()
    end_time = time.time()
    return result, end_time - start_time

@measure
def time_me():
    time.sleep(1)

if __name__ == "__main__":
    print(measure(lambda: time.sleep(1)))
