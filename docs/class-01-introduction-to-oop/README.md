# Class 01 – Introduction to Object-Oriented Programming

## What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around **objects** rather than functions and logic. An object can be defined as a data field with unique attributes and behaviour.

OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them.

---

## Core Principles

| Principle | Description |
|-----------|-------------|
| **Encapsulation** | Bundling data and the methods that operate on it inside a class, hiding internal details. |
| **Inheritance** | A mechanism where a new class (child) acquires the properties and behaviour of an existing class (parent). |
| **Polymorphism** | The ability of different objects to respond to the same message (method call) in different ways. |
| **Abstraction** | Hiding complex implementation details and showing only the essential features of an object. |

---

## Key Concepts

### Class
A **class** is a blueprint or template for creating objects. It defines a set of attributes (fields) and behaviours (methods) that the created objects will have.

```java
public class Animal {
    String name;
    int age;

    void makeSound() {
        System.out.println("...");
    }
}
```

### Object
An **object** is an instance of a class. Every object has a **state** (stored in attributes) and **behaviour** (expressed through methods).

```java
Animal dog = new Animal();
dog.name = "Rex";
dog.age  = 3;
dog.makeSound();
```

---

## Advantages of OOP

- **Modularity** – Each object forms a separate entity whose internal workings are decoupled from other parts.
- **Reusability** – Classes can be reused across multiple projects.
- **Scalability** – Large systems become easier to manage.
- **Maintainability** – Isolated changes reduce the risk of breaking unrelated code.

---

## References

- Bloch, J. (2018). *Effective Java* (3rd ed.). Addison-Wesley.
- Oracle. (2024). *The Java Tutorials – Object-Oriented Programming Concepts*. https://docs.oracle.com/javase/tutorial/java/concepts/index.html
