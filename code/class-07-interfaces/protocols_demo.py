"""
protocols_demo.py

Class 07 – Protocols and Duck Typing
(Python's equivalent of interfaces)

Demonstrates:
  - typing.Protocol as a structural interface (Python 3.8+)
  - Duck typing — any object with the right methods satisfies the protocol
  - runtime_checkable protocol with isinstance()
  - Combining multiple protocols
  - Callable / function as a "functional interface" equivalent
"""
from typing import Protocol, runtime_checkable


# ── Protocols (structural interfaces) ────────────────────────────────────────

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...


@runtime_checkable
class Resizable(Protocol):
    def resize(self, factor: float) -> None: ...


class Colorable(Protocol):
    def set_color(self, color: str) -> None: ...
    def get_color(self) -> str: ...


# ── Implementing classes ──────────────────────────────────────────────────────

class Circle:
    def __init__(self, radius: float, color: str) -> None:
        self.__radius = radius
        self.__color  = color

    def draw(self) -> None:
        print(f"Drawing Circle  [radius={self.__radius:.1f}, color={self.__color}]")

    def resize(self, factor: float) -> None:
        self.__radius *= factor
        print(f"Circle resized. New radius={self.__radius:.1f}")

    def set_color(self, color: str) -> None: self.__color = color
    def get_color(self) -> str:              return self.__color


class Square:
    def __init__(self, side: float, color: str) -> None:
        self.__side  = side
        self.__color = color

    def draw(self) -> None:
        print(f"Drawing Square  [side={self.__side:.1f}, color={self.__color}]")

    def resize(self, factor: float) -> None:
        self.__side *= factor
        print(f"Square resized. New side={self.__side:.1f}")

    def set_color(self, color: str) -> None: self.__color = color
    def get_color(self) -> str:              return self.__color


# ── Helper that accepts any Drawable ─────────────────────────────────────────

def render_all(drawables: list[Drawable]) -> None:
    for obj in drawables:
        obj.draw()


# ── Functional interface equivalent (callable) ───────────────────────────────

# In Python, a plain callable replaces @FunctionalInterface
Validator = callable   # type alias hint — any callable(str) -> bool

def run_validator(validator, value: str) -> bool:
    return validator(value)


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    shapes: list[Drawable] = [
        Circle(5.0, "red"),
        Square(3.0, "blue"),
    ]

    print("=== Drawing Shapes ===")
    render_all(shapes)

    print("\n=== Resizing & Recoloring ===")
    c = Circle(4.0, "green")
    c.resize(2.0)
    c.set_color("yellow")
    c.draw()

    # isinstance with @runtime_checkable
    print("\n=== Protocol isinstance checks ===")
    print(f"Circle is Drawable : {isinstance(c, Drawable)}")
    print(f"Circle is Resizable: {isinstance(c, Resizable)}")

    # Functional validators (lambdas)
    print("\n=== Validators ===")
    not_empty    = lambda s: len(s) > 0
    is_email     = lambda s: "@" in s
    short_enough = lambda s: len(s) <= 20

    test = "student@university.edu"
    print(f"not_empty    : {run_validator(not_empty,    test)}")
    print(f"is_email     : {run_validator(is_email,     test)}")
    print(f"short_enough : {run_validator(short_enough, test)}")
