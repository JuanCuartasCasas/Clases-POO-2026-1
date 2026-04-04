"""
inheritance_demo.py

Class 04 – Inheritance

Demonstrates:
  - Parent class with shared attributes and methods
  - Child classes using inheritance (implicit in Python via parentheses)
  - super() to call the parent __init__ and override methods
  - Method overriding with extended behaviour
"""


# ── Parent class ─────────────────────────────────────────────────────────────

class Animal:
    """Base class for all animals."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age  = age

    def eat(self) -> None:
        print(f"{self.name} is eating.")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping.")

    def __str__(self) -> str:
        return f"Animal[name={self.name}, age={self.age}]"


# ── Dog (child) ───────────────────────────────────────────────────────────────

class Dog(Animal):
    """A dog that extends Animal."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)   # call Animal.__init__
        self.breed = breed

    def bark(self) -> None:
        print(f"{self.name} says: Woof!")

    def eat(self) -> None:          # override
        super().eat()               # reuse parent behaviour …
        print(f"{self.name} wags its tail while eating.")   # … then extend it

    def __str__(self) -> str:
        return f"Dog[name={self.name}, age={self.age}, breed={self.breed}]"


# ── Cat (child) ───────────────────────────────────────────────────────────────

class Cat(Animal):
    """A cat that extends Animal."""

    def __init__(self, name: str, age: int, is_indoor: bool = True) -> None:
        super().__init__(name, age)
        self.is_indoor = is_indoor

    def purr(self) -> None:
        print(f"{self.name} purrs contentedly.")

    def eat(self) -> None:          # override
        print(f"{self.name} eats very delicately.")

    def __str__(self) -> str:
        return f"Cat[name={self.name}, age={self.age}, indoor={self.is_indoor}]"


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    dog = Dog("Rex",      3, "Labrador")
    cat = Cat("Whiskers", 5, is_indoor=True)

    print(dog)
    dog.eat()
    dog.bark()
    dog.sleep()

    print()

    print(cat)
    cat.eat()
    cat.purr()
    cat.sleep()

    # isinstance checks
    print()
    print(f"dog is Animal? {isinstance(dog, Animal)}")   # True
    print(f"cat is Dog?    {isinstance(cat, Dog)}")      # False
