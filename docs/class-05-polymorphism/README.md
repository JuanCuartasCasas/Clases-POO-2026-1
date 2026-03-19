# Class 05 – Polymorphism

## What is Polymorphism?

**Polymorphism** (Greek: *many forms*) allows objects of different classes to be treated uniformly through a common interface. The correct method is called based on the **actual type** of the object at runtime.

---

## Types of Polymorphism in Python

### 1. Duck Typing (Python's primary form)

> "If it walks like a duck and quacks like a duck, it's a duck."

Python does not check types at compile time. Any object that has the required method can be used:

```python
class Dog:
    def speak(self): print("Woof!")

class Cat:
    def speak(self): print("Meow!")

class Duck:
    def speak(self): print("Quack!")

animals = [Dog(), Cat(), Duck()]
for a in animals:
    a.speak()   # each responds differently — no shared base class needed
```

### 2. Method Overriding (Runtime Polymorphism)

Subclasses override a parent method; the right version is chosen at runtime:

```python
class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self) -> float: return 3.14159 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self) -> float: return self.w * self.h
```

### 3. Operator Overloading (Compile-time Polymorphism equivalent)

Define dunder methods to make operators work on your objects:

```python
class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
```

---

## Polymorphic Collections

```python
shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(f"Area: {s.area():.2f}")   # correct method called for each type
```

---

## Benefits

- Write generic code that works with many types.
- Add new types without modifying existing code (Open/Closed Principle).
- Cleaner, more readable code.

---

## References

- Lutz, M. (2013). *Learning Python* (5th ed.), Chapter 31. O'Reilly.

