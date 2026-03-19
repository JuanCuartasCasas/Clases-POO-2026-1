# Class 06 – Abstraction

## What is Abstraction?

**Abstraction** means hiding the complex internal implementation details and exposing only the essential features to the user. It lets you focus on **what** an object does instead of **how** it does it.

> A car driver uses the steering wheel and pedals without knowing how the engine works internally.

---

## Achieving Abstraction in Java

Java provides two mechanisms:

| Mechanism | Abstraction Level |
|-----------|-------------------|
| Abstract Classes | Partial (0–100 %) |
| Interfaces | Full (100 %) – prior to Java 8 default methods |

---

## Abstract Classes

- Declared with the `abstract` keyword.
- Can have both **abstract methods** (no body) and **concrete methods** (with body).
- **Cannot be instantiated** directly.
- Subclasses **must** implement all abstract methods (unless they are also abstract).

```java
public abstract class Shape {
    private String color;

    public Shape(String color) {
        this.color = color;
    }

    // Abstract method – no body
    public abstract double area();

    // Concrete method – has body
    public String getColor() {
        return color;
    }
}
```

### Concrete Subclass

```java
public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}
```

---

## When to Use Abstract Classes

- You want to share code among closely related classes.
- You need to define non-static, non-final fields.
- You want to provide a common base with some default behaviour.

---

## Abstract Class vs Interface

| Feature | Abstract Class | Interface |
|---------|---------------|-----------|
| Multiple inheritance | ❌ | ✅ |
| Fields | ✅ (any type) | Only `public static final` |
| Constructors | ✅ | ❌ |
| Default methods | ✅ (concrete) | ✅ (since Java 8) |
| Use-case | "is-a" base type | "can-do" contract |

---

## References

- Oracle. (2024). *Abstract Methods and Classes*. https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html
