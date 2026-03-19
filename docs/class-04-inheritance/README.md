# Class 04 – Inheritance

## What is Inheritance?

**Inheritance** is the mechanism by which one class (child / subclass) acquires the attributes and methods of another class (parent / superclass). It promotes **code reuse** and establishes an **"is-a"** relationship.

```
Animal  ←  Dog
Animal  ←  Cat
```

*A Dog **is an** Animal.*

---

## Syntax in Python

```python
# Parent class
class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age  = age

    def eat(self) -> None:
        print(f"{self.name} is eating.")


# Child class
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)   # call parent __init__
        self.breed = breed

    def bark(self) -> None:
        print(f"{self.name} says: Woof!")
```

---

## `super()`

`super()` returns a proxy object that delegates method calls to the parent class. The most common use is calling the parent constructor:

```python
super().__init__(name, age)
```

---

## Method Overriding

A subclass can **override** a parent method to provide a specialised implementation:

```python
class Cat(Animal):
    def eat(self) -> None:       # overrides Animal.eat
        print(f"{self.name} eats very delicately.")
```

To extend (not replace) the parent behaviour, call `super()`:

```python
class Dog(Animal):
    def eat(self) -> None:
        super().eat()            # run Animal.eat first
        print(f"{self.name} wags its tail.")
```

---

## Types of Inheritance (Python)

| Type | Supported? |
|------|------------|
| Single | ✅ |
| Multilevel | ✅ |
| Hierarchical | ✅ |
| Multiple | ✅ (via MRO – Method Resolution Order) |

```python
class A: ...
class B(A): ...
class C(A): ...
class D(B, C): ...   # multiple inheritance — Python uses C3 linearisation
```

---

## `isinstance()` and `issubclass()`

```python
dog = Dog("Rex", 3, "Labrador")
isinstance(dog, Dog)     # True
isinstance(dog, Animal)  # True  — inheritance chain
issubclass(Dog, Animal)  # True
```

---

## Composition vs. Inheritance

> **Favour composition over inheritance** when the relationship is "has-a", not "is-a".

| Inheritance | Composition |
|-------------|-------------|
| "is-a" | "has-a" |
| Tight coupling | Loose coupling |

---

## References

- Python Docs. (2024). *Inheritance*. https://docs.python.org/3/tutorial/classes.html#inheritance

