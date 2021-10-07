import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self) -> float:
        """Provide the area of the shape."""

    # @abc.abstractmethod
    # def circumference(self) -> float:
    #     """Provide the circumference of the shape.
    #     """
