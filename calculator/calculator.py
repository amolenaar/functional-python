import operator

OPERATORS = {
    '+': operator.add,
    '-': lambda a, b: a - b,
    '*': operator.mul,
}


def calculate(a, op, b):
    return OPERATORS[op](a, b)



def partial_calculator(a):
    def _partial_oper(op):
        def _partial_b(b):
            return calculate(a, op, b)
        return  _partial_b
    return  _partial_oper



# How to do this without state modification?
def lazy_calculator(iterable):
    calc = partial_calculator
    while True:
        val = next(iterable)

        calc = calc(val)
        if not callable(calc):
            yield calc
            calc = partial_calculator(calc)


def maybe_int(val):
    try:
        return int(val)
    except ValueError:
        return val


def input_generator():
    while True:
        yield maybe_int(input("in> "))


def printer(iterable):
    while True:
        val = next(iterable)
        print("-->", val)


class binding:
    def __init__(self, func):
        self._func = func

    def __or__(self, func):
        return binding(func(self._func))


if __name__ == "__main__":
    # printer(lazy_calculator(input_generator()))
    
    binding(input_generator()) | lazy_calculator | printer
