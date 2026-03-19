# Problem 02 – Shape Calculator ⭐⭐⭐

## Context

Build a **shape calculator** that can handle multiple geometric shapes, report their properties, and sort them. This problem combines abstraction, polymorphism, and interfaces.

---

## Requirements

### Abstract Class: `Shape`

| Member | Details |
|--------|---------|
| `color` | `String` |
| `area()` | **Abstract** `double` |
| `perimeter()` | **Abstract** `double` |
| `describe()` | Concrete – prints shape info (type, color, area, perimeter) |

### Interface: `Printable`

```java
interface Printable {
    void printDetails();
}
```

### Interface: `Scalable`

```java
interface Scalable {
    Shape scale(double factor); // returns a NEW scaled shape
}
```

### Concrete Shapes

Implement: `Circle`, `Rectangle`, `Triangle`, `Hexagon`.

All must extend `Shape` and implement `Printable` and `Scalable`.

### Class: `ShapeCalculator`

| Method | Details |
|--------|---------|
| `addShape(Shape s)` | Adds shape to internal list |
| `totalArea()` | Sum of all areas |
| `totalPerimeter()` | Sum of all perimeters |
| `largestShape()` | Shape with maximum area |
| `smallestShape()` | Shape with minimum area |
| `sortByArea()` | Returns shapes sorted ascending by area |
| `printAllShapes()` | Prints details of every shape |

### Class: `ShapeDemo`

- Create at least **2 shapes of each type**.
- Add them all to a `ShapeCalculator`.
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
Largest shape  : Circle [red] area=78.54
Smallest shape : Rectangle [blue] area=24.00

=== Sorted by Area ===
1. Rectangle [blue] 24.00
2. Triangle  [green] 37.50
...
```

---

## Hints

- Use `Comparator.comparingDouble(Shape::area)` for sorting.
- The `scale(factor)` method should return a **new object**, not modify the existing one (immutable operation).
- Override `toString()` for clean output in sorted list.
