# Problem 02 – Shape Calculator ⭐⭐⭐

## Context

Build a **shape calculator** that can handle multiple geometric shapes, report their properties, and sort them. This problem combines abstraction, polymorphism, and protocols.

---

## Requirements

### Abstract Class: `Shape`

| Member | Details |
|--------|---------|
| `color` | `str` |
| `area()` | **Abstract** `-> float` |
| `perimeter()` | **Abstract** `-> float` |
| `describe()` | Concrete – prints shape info (type, color, area, perimeter) |

Use `from abc import ABC, abstractmethod`.

### Protocol: `Scalable`

```python
from typing import Protocol

class Scalable(Protocol):
    def scale(self, factor: float) -> "Shape": ...
    # Returns a NEW scaled shape (immutable operation)
```

### Concrete Shapes

Implement: `Circle`, `Rectangle`, `Triangle`, `Hexagon`.

All must extend `Shape` and implement `scale()`.

### Class: `ShapeCalculator`

| Method | Details |
|--------|---------|
| `add_shape(shape)` | Adds shape to internal list |
| `total_area` | Property — sum of all areas |
| `total_perimeter` | Property — sum of all perimeters |
| `largest_shape()` | Shape with maximum area |
| `smallest_shape()` | Shape with minimum area |
| `sort_by_area()` | Returns shapes sorted ascending by area |
| `print_all_shapes()` | Prints details of every shape |

### Script (`shape_demo.py`)

- Create at least **2 shapes of each type**.
- Add them to a `ShapeCalculator`.
- Print total area, largest/smallest shape, and sorted list.

---

## Expected Output (Example)

```
=== Shape Report ===
Circle    [red]    area=78.54  perimeter=31.42
Rectangle [blue]   area=24.00  perimeter=20.00
...

Total area     : 245.71
Total perimeter: 130.88
Largest : Circle [red] area=78.54
Smallest: Rectangle [blue] area=24.00

=== Sorted by Area ===
1. Rectangle [blue] 24.00
2. Triangle  [green] 37.50
...
```

---

## Hints

- Use `sorted(self.__shapes, key=lambda s: s.area())` for sorting.
- The `scale(factor)` method must return a **new object**, not modify the existing one.
- Use `max()` / `min()` with `key=lambda s: s.area()` for largest/smallest.
- Use `@property` for `total_area` and `total_perimeter`.

