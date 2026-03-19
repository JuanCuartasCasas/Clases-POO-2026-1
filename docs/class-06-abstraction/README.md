# Class 06 – Abstraction

## What is Abstraction?

**Abstraction** means hiding the complex internal implementation details and exposing only the essential features. It lets you focus on **what** an object does instead of **how** it does it.

> A car driver uses the steering wheel and pedals without knowing how the engine works internally.

---

## Achieving Abstraction in Python

Python provides the `abc` module (Abstract Base Classes):

```python
from abc import ABC, abstractmethod
```

| Mechanism | Abstraction Level |
|-----------|-------------------|
| Abstract Base Class (ABC) | Partial or full |
| Protocol (structural) | Full (duck typing) |

---

## Abstract Classes

- Inherit from `ABC`.
- Decorate methods with `@abstractmethod` to force subclasses to implement them.
- **Cannot be instantiated** directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color: str) -> None:
        self.color = color

    @abstractmethod
    def area(self) -> float: ...      # no body — subclass must implement

    @abstractmethod
    def perimeter(self) -> float: ... # no body

    def describe(self) -> None:       # concrete shared behaviour
        print(f"{type(self).__name__} [color={self.color}]  area={self.area():.2f}")
```

### Concrete Subclass

```python
import math

class Circle(Shape):
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
```

---

## Trying to Instantiate an Abstract Class

```python
s = Shape("red")   # TypeError: Can't instantiate abstract class Shape
```

---

## When to Use Abstract Classes

- Share code among closely related classes.
- Enforce a common interface that all subclasses must implement.
- Provide default concrete behaviour alongside abstract methods.

---

## Abstract Class vs Protocol

| Feature | Abstract Class (ABC) | Protocol |
|---------|---------------------|----------|
| Explicit inheritance | Required | Not required |
| Runtime `isinstance` | ✅ | ✅ (if `@runtime_checkable`) |
| Enforcement | `@abstractmethod` | Static type checkers |
| Use-case | "is-a" hierarchy | Structural / duck typing |

---

## References

- Python Docs. (2024). *abc — Abstract Base Classes*. https://docs.python.org/3/library/abc.html

