"""
abstraction_demo.py

Class 06 – Abstraction

Demonstrates:
  - Abstract Base Classes (ABC) from the `abc` module
  - @abstractmethod forces subclasses to implement required methods
  - Concrete shared behaviour in the abstract base
  - Working with abstract type references
"""
from abc import ABC, abstractmethod


# ── Abstract base ─────────────────────────────────────────────────────────────

class Vehicle(ABC):
    """Abstract vehicle — cannot be instantiated directly."""

    def __init__(self, brand: str, year: int) -> None:
        self._brand = brand   # protected convention
        self._year  = year

    # Abstract — every vehicle type MUST define these
    @abstractmethod
    def start_engine(self) -> None: ...

    @abstractmethod
    def max_speed(self) -> int: ...   # km/h

    # Concrete — shared behaviour
    def display_info(self) -> None:
        print(f"{self._year} {self._brand}  (max {self.max_speed()} km/h)")

    @property
    def brand(self) -> str: return self._brand

    @property
    def year(self) -> int:  return self._year


# ── Concrete subclasses ───────────────────────────────────────────────────────

class ElectricCar(Vehicle):
    def __init__(self, brand: str, year: int, battery_kwh: int) -> None:
        super().__init__(brand, year)
        self.__battery_kwh = battery_kwh

    def start_engine(self) -> None:
        print(f"{self._brand}: Electric motor activated silently.")

    def max_speed(self) -> int:
        return 250

    @property
    def battery_capacity(self) -> int:
        return self.__battery_kwh


class GasolineMotorcycle(Vehicle):
    def __init__(self, brand: str, year: int, cylinder_cc: int) -> None:
        super().__init__(brand, year)
        self.__cylinder_cc = cylinder_cc

    def start_engine(self) -> None:
        print(f"{self._brand}: Vroom! {self.__cylinder_cc}cc engine started.")

    def max_speed(self) -> int:
        return 180


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Cannot instantiate Vehicle directly
    # v = Vehicle("X", 2024)  # TypeError!

    fleet: list[Vehicle] = [
        ElectricCar("Tesla",   2024, battery_kwh=100),
        GasolineMotorcycle("Honda", 2023, cylinder_cc=600),
    ]

    for vehicle in fleet:
        vehicle.display_info()
        vehicle.start_engine()
        print()

    # Downcast to access subclass-specific attribute
    ev = fleet[0]
    if isinstance(ev, ElectricCar):
        print(f"Battery capacity: {ev.battery_capacity} kWh")
