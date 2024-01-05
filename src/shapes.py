import math


class Shape(object):
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.length == other.length and self.width == other.width
    
    def area(self) -> float:
        return self.length * self.width
    
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side_length: int) -> None:
        super().__init__(length=side_length, width=side_length)