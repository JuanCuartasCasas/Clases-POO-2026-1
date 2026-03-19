# Class 07 – Protocols and Duck Typing

## What is a Protocol?

In Python, a **Protocol** (from `typing`) is a way to define a **structural interface** — a contract that any class can satisfy simply by having the right methods and attributes, without explicitly inheriting from it.

This is Python's equivalent of interfaces in Java/C#, but more flexible because it follows **duck typing**.

---

## Defining a Protocol

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...
```

Any class that has a `draw(self) -> None` method automatically satisfies `Drawable`, even if it doesn't inherit from it.

---

## Implementing (Satisfying) a Protocol

No explicit declaration needed:

```python
class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())   # works
render(Square())   # works
```

---

## `@runtime_checkable`

Add this decorator to allow `isinstance()` checks at runtime:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

c = Circle()
print(isinstance(c, Drawable))   # True
```

---

## Multiple Protocols

A class can satisfy multiple protocols at once:

```python
class Resizable(Protocol):
    def resize(self, factor: float) -> None: ...

class Circle:
    def draw(self)              -> None: ...
    def resize(self, factor)    -> None: ...
    # Satisfies BOTH Drawable and Resizable
```

---

## Duck Typing vs Protocol

| Duck Typing | Protocol |
|------------|---------|
| No type hints | Uses `typing.Protocol` |
| No static checking | Checked by mypy / Pyright |
| Most Pythonic | More structured / explicit |

---

## Callable as Functional Interface

Python functions are first-class objects and can replace single-method interfaces:

```python
# Instead of a Validator class/interface:
not_empty: callable = lambda s: len(s) > 0

def validate(value: str, validator) -> bool:
    return validator(value)

print(validate("hello", not_empty))   # True
```

---

## References

- Python Docs. (2024). *typing.Protocol*. https://docs.python.org/3/library/typing.html#typing.Protocol
- van Rossum, G. et al. (2015). *PEP 544 – Protocols: Structural subtyping*. https://peps.python.org/pep-0544/

