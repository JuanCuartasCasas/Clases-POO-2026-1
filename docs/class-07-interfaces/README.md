# Class 07 – Interfaces

## What is an Interface?

An **interface** is a completely abstract type that defines a **contract** — a set of method signatures that implementing classes must fulfil. It expresses a **"can-do"** or **"behaves-like"** relationship.

---

## Declaring an Interface

```java
public interface Drawable {
    void draw();                    // abstract by default
    default void printInfo() {      // default method (Java 8+)
        System.out.println("I am drawable.");
    }
}
```

---

## Implementing an Interface

A class uses the `implements` keyword. It must provide a body for every abstract method.

```java
public class Rectangle implements Drawable {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width  = width;
        this.height = height;
    }

    @Override
    public void draw() {
        System.out.println("Drawing a rectangle " + width + " x " + height);
    }
}
```

---

## Multiple Interfaces

A class can implement **multiple interfaces** (unlike class inheritance in Java):

```java
public interface Resizable {
    void resize(double factor);
}

public class Circle implements Drawable, Resizable {
    private double radius;

    public Circle(double radius) { this.radius = radius; }

    @Override
    public void draw()                   { System.out.println("Drawing circle r=" + radius); }

    @Override
    public void resize(double factor)    { radius *= factor; }
}
```

---

## Interface vs Abstract Class (Quick Reference)

| Feature | Interface | Abstract Class |
|---------|-----------|----------------|
| Multiple inheritance | ✅ | ❌ |
| Fields | `public static final` only | Any |
| Constructors | ❌ | ✅ |
| Default methods | ✅ (Java 8+) | ✅ |
| Relationship | "can-do" | "is-a" |

---

## Functional Interfaces & Lambdas (Java 8+)

A **functional interface** has exactly one abstract method and can be used with lambda expressions.

```java
@FunctionalInterface
public interface Validator {
    boolean validate(String input);
}

Validator notEmpty = input -> !input.isEmpty();
System.out.println(notEmpty.validate("hello")); // true
```

---

## Common Built-in Interfaces

| Interface | Package | Purpose |
|-----------|---------|---------|
| `Comparable<T>` | `java.lang` | Natural ordering (`compareTo`) |
| `Iterable<T>` | `java.lang` | For-each iteration |
| `Runnable` | `java.lang` | Thread task |
| `Serializable` | `java.io` | Object serialization marker |
| `List<E>` | `java.util` | Ordered collection contract |

---

## References

- Oracle. (2024). *Interfaces*. https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html
