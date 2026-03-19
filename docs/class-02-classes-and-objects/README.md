# Class 02 – Classes and Objects

## Classes

A **class** is a user-defined data type. It acts as a blueprint from which individual objects are created.

### Anatomy of a Class

```python
class ClassName:
    # Class attribute (shared by all instances)
    species = "unknown"

    def __init__(self, param1, param2):   # constructor
        self.param1 = param1              # instance attribute
        self.param2 = param2

    def some_method(self):               # behaviour
        pass
```

### Example

```python
class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year  = year

    def display_info(self) -> None:
        print(f"{self.year} {self.brand} {self.model}")
```

---

## Objects

An **object** is a runtime instance of a class created by calling it like a function.

```python
my_car = Car("Toyota", "Corolla", 2024)
my_car.display_info()   # 2024 Toyota Corolla
```

### Object Identity vs Equality

| Concept | Operator / Method | Checks |
|---------|-------------------|--------|
| Identity | `is` | Same object in memory |
| Equality | `==` | Same value (uses `__eq__`) |

---

## `__init__` (Constructor)

`__init__` is called automatically when a new object is created. Use it to set up instance attributes.

```python
class Car:
    def __init__(self, brand="Unknown", model="Unknown", year=0):
        self.brand = brand
        self.model = model
        self.year  = year
```

---

## `self`

`self` refers to the current object instance. It must be the **first parameter** of every instance method, though you never pass it explicitly when calling.

---

## Special (Dunder) Methods

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor |
| `__str__` | Human-readable string (`print(obj)`) |
| `__repr__` | Developer-readable string |
| `__eq__` | Equality comparison (`==`) |

```python
def __str__(self) -> str:
    return f"{self.year} {self.brand} {self.model}"
```

---

## Memory

- All objects live on the **heap**.
- Variables hold **references** (pointers) to objects, not the objects themselves.

---

## References

- Lutz, M. (2013). *Learning Python* (5th ed.), Chapter 27. O'Reilly.

