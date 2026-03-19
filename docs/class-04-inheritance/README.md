# Class 04 – Inheritance

## What is Inheritance?

**Inheritance** is the mechanism by which one class (child / subclass) acquires the fields and methods of another class (parent / superclass). It promotes **code reuse** and establishes an **"is-a"** relationship.

```
Animal  ←  Dog
Animal  ←  Cat
```

*A Dog **is an** Animal.*

---

## Syntax in Java

```java
// Parent class
public class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }
}

// Child class
public class Dog extends Animal {
    private String breed;

    public Dog(String name, String breed) {
        super(name);          // calls Animal constructor
        this.breed = breed;
    }

    public void bark() {
        System.out.println(name + " says: Woof!");
    }
}
```

---

## The `super` Keyword

| Usage | Purpose |
|-------|---------|
| `super(args)` | Calls the parent constructor (must be first statement) |
| `super.method()` | Calls an overridden method from the parent |

---

## Method Overriding

A subclass can **override** a parent method to provide a specialised implementation. Use `@Override` annotation for compiler validation.

```java
public class Cat extends Animal {
    public Cat(String name) { super(name); }

    @Override
    public void eat() {
        System.out.println(name + " eats delicately.");
    }
}
```

---

## Types of Inheritance (Java)

| Type | Supported in Java? |
|------|--------------------|
| Single | ✅ |
| Multilevel | ✅ |
| Hierarchical | ✅ |
| Multiple (classes) | ❌ (use interfaces) |

---

## `final` Classes and Methods

- `final class` – Cannot be extended.
- `final method` – Cannot be overridden.

---

## Composition vs. Inheritance

> **Favour composition over inheritance** (Effective Java, Item 18).

| Inheritance | Composition |
|-------------|-------------|
| "is-a" relationship | "has-a" relationship |
| Tight coupling | Loose coupling |
| Harder to change | Easier to change |

---

## References

- Bloch, J. (2018). *Effective Java* (3rd ed.), Item 18. Addison-Wesley.
