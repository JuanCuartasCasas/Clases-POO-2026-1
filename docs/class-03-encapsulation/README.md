# Class 03 – Encapsulation

## What is Encapsulation?

**Encapsulation** is the OOP principle of bundling data (fields) and the methods that operate on that data within a single unit (class), while restricting direct access to some components.

> "Don't expose internal state; expose behaviour."

---

## Access Modifiers in Java

| Modifier | Same Class | Same Package | Subclass | Anywhere |
|----------|-----------|--------------|----------|----------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| (default) | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

---

## Getters and Setters

To safely expose private fields, provide **getter** and **setter** methods:

```java
public class BankAccount {
    private double balance;

    // Getter
    public double getBalance() {
        return balance;
    }

    // Setter with validation
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }
}
```

---

## Benefits of Encapsulation

1. **Control** – You decide what data can be read or modified.
2. **Validation** – Setters can enforce business rules (e.g., no negative balance).
3. **Flexibility** – Internal implementation can change without affecting external code.
4. **Security** – Sensitive data is hidden from external classes.

---

## Immutable Objects

An object is **immutable** when its state cannot change after construction. Achieve this by:
- Making all fields `private final`.
- Providing no setters.
- Returning copies of mutable fields in getters.

```java
public final class Point {
    private final int x;
    private final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() { return x; }
    public int getY() { return y; }
}
```

---

## References

- Oracle. (2024). *Controlling Access to Members of a Class*. https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html
