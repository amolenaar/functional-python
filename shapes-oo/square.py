from shape import Shape


class Square(Shape):
    def __init__(self, side: float):
        self._side = side

    def area(self) -> float:
        return self._side * self._side
