# Exercise 01 – Tracing Objects

## Code

```python
class Counter:
    def __init__(self, initial: int) -> None:
        self.__count = initial

    def increment(self) -> None:
        self.__count += 1

    def decrement(self) -> None:
        self.__count -= 1

    def get_count(self) -> int:
        return self.__count

    def __str__(self) -> str:
        return f"Counter({self.__count})"


if __name__ == "__main__":
    a = Counter(0)
    b = Counter(10)
    c = a              # (*)

    a.increment()
    a.increment()
    b.decrement()
    c.increment()      # (**)

    print(a)
    print(b)
    print(c)
    print(a is c)
```

---

## Questions

Answer **before** running the code.

1. How many `Counter` objects are created in this program?
2. What does `print(a)` output after all operations?
3. What does `print(b)` output after all operations?
4. After line `(**)`, does `a.get_count()` equal `c.get_count()`? Why?
5. What does `a is c` print? What does this tell you about object references in Python?

---

## Answers

> Fill in after your analysis, then verify by running the code.

1. ___
2. ___
3. ___
4. ___
5. ___

---

## Key Takeaways

- `c = a` does **not** create a new object — it copies the **reference** (both names point to the same object).
- Any mutation through `c` is visible via `a` (and vice versa).
- `is` checks **identity** (same object in memory), not equality of value.
- `==` checks **equality** (value), which uses `__eq__` (falls back to identity if not defined).

