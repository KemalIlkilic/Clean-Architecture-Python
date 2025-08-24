# This design violates Open-Closed Principle.

class Rectangle():
    def __init__(self, width : int, height: int):
        self.width = width
        self.height = height

class Circle():
    def __init__(self, radius : int):
        self.radius = radius


class AreaCalculator():
    def calculate_area(self, shape):
        if isinstance(shape,Rectangle):
            return shape.width * shape.width * (0.5)
        
        if isinstance(shape,Circle):
            return 3.14 * shape.radius ** 2
        
        else:
            raise ValueError("Unsupported Shape")
# Usage
rectangle = Rectangle(5, 4)
circle = Circle(3)
calculator = AreaCalculator()
print(f"Rectangle area: {calculator.calculate_area(rectangle)}")
print(f"Circle area: {calculator.calculate_area(circle)}")