"""
polymorphism_demo.py

Class 05 – Polymorphism

Demonstrates:
  - Runtime polymorphism via method overriding
  - Duck typing (Python's natural form of polymorphism)
  - isinstance() checks
  - A list of mixed objects treated uniformly
"""
import math


# ── Base class ────────────────────────────────────────────────────────────────

class Shape:
    """Abstract-like base for geometric shapes."""

    def __init__(self, color: str) -> None:
        self.color = color

    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self) -> float:
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self) -> None:
        print(
            f"{type(self).__name__:<12} [color={self.color}]"
            f"  area={self.area():.2f}  perimeter={self.perimeter():.2f}"
        )


# ── Concrete shapes ───────────────────────────────────────────────────────────

class Circle(Shape):
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self)      -> float: return math.pi * self.radius ** 2
    def perimeter(self) -> float: return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float) -> None:
        super().__init__(color)
        self.width  = width
        self.height = height

    def area(self)      -> float: return self.width * self.height
    def perimeter(self) -> float: return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, color: str, a: float, b: float, c: float) -> None:
        super().__init__(color)
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Heron

    def perimeter(self) -> float: return self.a + self.b + self.c


# ── Duck typing demo ──────────────────────────────────────────────────────────

class Printer:
    """Overloaded print – Python handles this via default args / *args."""

    def print_value(self, value) -> None:
        print(f"{type(value).__name__}: {value}")


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Polymorphic collection
    shapes: list[Shape] = [
        Circle("red",    5.0),
        Rectangle("blue",  4.0, 6.0),
        Triangle("green",  3.0, 4.0, 5.0),
    ]

    print("=== All Shapes ===")
    for shape in shapes:
        shape.describe()    # correct method called at runtime

    # isinstance check
    print("\n=== isinstance ===")
    for shape in shapes:
        print(f"{type(shape).__name__} is Shape: {isinstance(shape, Shape)}")

    # Duck typing – anything with area() and perimeter() works
    print("\n=== Duck Typing Demo ===")

    class HexagonDuck:
        """Not a subclass of Shape, but has the same interface."""
        def area(self)      -> float: return 37.1
        def perimeter(self) -> float: return 24.0

    duck = HexagonDuck()
    for obj in [Circle("purple", 2.0), duck]:
        print(f"area={obj.area():.2f}  perimeter={obj.perimeter():.2f}")

    # Overloading via default args
    print("\n=== Printer ===")
    p = Printer()
    p.print_value(42)
    p.print_value(3.14)
    p.print_value("Hello OOP")
