# Challenge 03 – Animal Hierarchy ⭐⭐⭐

## Description

Build an **animal classification hierarchy** that demonstrates inheritance, method overriding, and polymorphism in Python.

---

## Requirements

### Abstract Class: `Animal`

| Member | Details |
|--------|---------|
| `name` | `str` |
| `age` | `int` |
| `make_sound()` | **Abstract** – each animal sounds different |
| `move()` | **Abstract** – each animal moves differently |
| `eat(food)` | Concrete – prints `"<name> eats <food>"` |
| `describe()` | Concrete – prints full info using `make_sound()` and `move()` |

Use `from abc import ABC, abstractmethod`.

### Concrete Classes

Implement at least **4 animals**: `Dog`, `Cat`, `Eagle`, `Fish`.

Each must override `make_sound()` and `move()` with realistic behaviour.

### Protocol / Mixin: `Trainable`

```python
class Trainable:
    def train(self, command: str) -> None: ...
    def can_learn_trick(self, trick: str) -> bool: ...
```

`Dog` and `Eagle` should inherit from `Trainable` (multiple inheritance).

### Class: `AnimalShelter`

| Member | Details |
|--------|---------|
| `__animals` | `list[Animal]`, private |
| `admit(animal)` | Adds an animal |
| `describe_all()` | Calls `describe()` on every animal |
| `get_trainable_animals()` | Returns filtered list of `Trainable` animals |

---

## Expected Output (Example)

```
Rex (Dog, 3)      | Sound: Woof!    | Move: Runs on four legs
Whiskers (Cat, 5) | Sound: Meow     | Move: Walks gracefully
Sky (Eagle, 2)    | Sound: Screech! | Move: Soars through the sky
Nemo (Fish, 1)    | Sound: ...      | Move: Swims with fins

Trainable animals: Rex, Sky
```

---

## Hints

- Use `isinstance(animal, Trainable)` to filter trainable animals.
- Multiple inheritance syntax: `class Dog(Animal, Trainable):`.
- Override `__str__` in each class for clean output.
- Use a list comprehension in `get_trainable_animals()`.

