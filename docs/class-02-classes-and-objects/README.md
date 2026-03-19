# Class 02 – Classes and Objects

## Classes

A **class** is a user-defined data type. It acts as a blueprint from which individual objects are created.

### Anatomy of a Class

```
[access modifier] class ClassName {
    // Fields (attributes / state)
    // Constructors
    // Methods (behaviour)
}
```

### Example

```java
public class Car {
    // Fields
    private String brand;
    private String model;
    private int year;

    // Constructor
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year  = year;
    }

    // Method
    public void displayInfo() {
        System.out.println(year + " " + brand + " " + model);
    }
}
```

---

## Objects

An **object** is a runtime instance of a class created with the `new` keyword.

```java
Car myCar = new Car("Toyota", "Corolla", 2024);
myCar.displayInfo(); // Output: 2024 Toyota Corolla
```

### Object Identity vs Equality

| Concept | Operator / Method | Checks |
|---------|-------------------|--------|
| Identity | `==` | Same memory reference |
| Equality | `.equals()` | Logically the same content |

---

## Constructors

A **constructor** is a special method called when an object is instantiated. It has the same name as the class and no return type.

```java
// Default (no-argument) constructor
public Car() {
    this.brand = "Unknown";
    this.model = "Unknown";
    this.year  = 0;
}

// Parameterised constructor
public Car(String brand, String model, int year) { ... }
```

---

## The `this` Keyword

`this` refers to the current object instance. It is commonly used to:
- Distinguish between instance fields and constructor/method parameters with the same name.
- Call another constructor within the same class (`this(...)`).

---

## Memory Layout

| Area | Stores |
|------|--------|
| **Stack** | Local variables, method calls, references |
| **Heap** | Actual object data allocated with `new` |

---

## References

- Sierra, K., & Bates, B. (2005). *Head First Java* (2nd ed.). O'Reilly.
