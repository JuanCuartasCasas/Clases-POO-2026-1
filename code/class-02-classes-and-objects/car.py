"""
car.py

Class 02 – Classes and Objects

Demonstrates:
  - Defining a class with private-by-convention attributes
  - Multiple constructors via default parameters
  - The use of `self`
  - __str__ / __repr__ overrides
"""


class Car:
    """Represents a car with brand, model, year, and price."""

    def __init__(
        self,
        brand: str  = "Unknown",
        model: str  = "Unknown",
        year: int   = 0,
        price: float = 0.0,
    ) -> None:
        self.brand = brand
        self.model = model
        self.year  = year
        self.price = price

    # Behaviour
    def display_info(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.year} {self.brand} {self.model} – ${self.price:,.2f}"

    def __repr__(self) -> str:
        return (
            f"Car(brand={self.brand!r}, model={self.model!r}, "
            f"year={self.year}, price={self.price})"
        )


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2024, 22_000.00)
    car2 = Car("Honda",  "Civic",   2023, 20_500.00)
    car3 = Car()  # default values

    car1.display_info()
    car2.display_info()
    car3.display_info()

    # Identity vs Equality
    car_a = Car("Toyota", "Corolla", 2024, 22_000.00)
    print(f"\ncar1 is car_a         : {car1 is car_a}")          # False
    print(f"car1 == car_a (default): {car1 == car_a}")           # False (no __eq__ override)
