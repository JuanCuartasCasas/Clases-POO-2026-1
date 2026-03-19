# Class 03 – Encapsulation

## What is Encapsulation?

**Encapsulation** is the OOP principle of bundling data (attributes) and the methods that operate on that data within a single unit (class), while restricting direct access to some components.

> "Don't expose internal state; expose behaviour."

---

## Attribute Privacy in Python

Python uses **naming conventions** and **name mangling** instead of strict access modifiers:

| Convention | Syntax | Meaning |
|------------|--------|---------|
| Public | `self.name` | Accessible from anywhere |
| Protected | `self._name` | Accessible, but "please don't touch" |
| Private | `self.__name` | Name-mangled to `_ClassName__name` |

---

## Properties (Getters & Setters)

Use the `@property` decorator to expose private attributes in a controlled way:

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.__owner   = owner
        self.__balance = balance

    @property
    def balance(self) -> float:       # getter
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
```

Usage:

```python
account = BankAccount("Alice", 1000)
print(account.balance)    # 1000  — reads via @property
account.deposit(500)
account.withdraw(200)
```

---

## Benefits of Encapsulation

1. **Control** – You decide what can be read or modified.
2. **Validation** – Logic in mutator methods enforces business rules.
3. **Flexibility** – Internal representation can change without breaking clients.
4. **Security** – Sensitive data is hidden.

---

## Immutable Objects

A class is effectively **immutable** when:
- All attributes are set in `__init__` and never changed.
- No setters are provided.
- Mutable attributes are returned as copies.

```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float: return self.__x

    @property
    def y(self) -> float: return self.__y

    def __repr__(self) -> str:
        return f"Point({self.__x}, {self.__y})"
```

---

## References

- Python Docs. (2024). *Private Variables*. https://docs.python.org/3/tutorial/classes.html#private-variables

