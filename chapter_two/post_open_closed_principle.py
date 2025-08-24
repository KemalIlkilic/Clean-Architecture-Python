from abc import ABC, abstractmethod
import math

#We can now add new shapes (such as Triangle) without modifying the AreaCalculator class. The system is open for extension but closed for modification.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width : float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.width

class Circle():
    def __init__(self, radius : float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class AreaCalculator():
    def calculate_area(self, shape: Shape):
        return shape.area()


rectangle = Rectangle(5, 4)
circle = Circle(3)
calculator = AreaCalculator()
print(f"Rectangle area: {calculator.calculate_area(rectangle)}")
print(f"Circle area: {calculator.calculate_area(circle)}")