"""
hello_oop.py

Class 01 – Introduction to Object-Oriented Programming

Demonstrates:
  - Defining a class with attributes and a method
  - Creating objects (instances)
  - Accessing object state and behaviour
"""


# ── A minimal class ──────────────────────────────────────────────────────────

class Animal:
    """A simple class representing an animal."""

    def __init__(self, name: str, sound: str) -> None:
        # Instance attributes (state)
        self.name  = name
        self.sound = sound

    # Method (behaviour)
    def make_sound(self) -> None:
        print(f"{self.name} says: {self.sound}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Create two objects from the same class blueprint
    dog = Animal("Rex",      "Woof")
    cat = Animal("Whiskers", "Meow")

    dog.make_sound()   # Rex says: Woof
    cat.make_sound()   # Whiskers says: Meow

    # Each object has its own independent state
    print(f"Dog name : {dog.name}")
    print(f"Cat name : {cat.name}")
