# Class 05 – Polymorphism

## What is Polymorphism?

**Polymorphism** (Greek: *many forms*) allows objects of different classes to be treated as objects of a common superclass. The correct method is selected at runtime based on the actual type of the object.

---

## Types of Polymorphism in Java

### 1. Compile-time Polymorphism (Method Overloading)

Multiple methods **share the same name** but differ in the number or type of parameters. Resolved at compile time.

```java
public class MathUtils {
    public int add(int a, int b)         { return a + b; }
    public double add(double a, double b){ return a + b; }
    public int add(int a, int b, int c)  { return a + b + c; }
}
```

### 2. Runtime Polymorphism (Method Overriding)

A subclass provides a specific implementation of a method already defined in the superclass. Resolved at runtime via **dynamic dispatch**.

```java
Animal a = new Dog("Rex", "Labrador");
a.makeSound(); // calls Dog's makeSound(), not Animal's
```

---

## Upcasting and Downcasting

```java
Animal a = new Dog("Rex", "Labrador");  // upcasting (implicit)
Dog d = (Dog) a;                        // downcasting (explicit)
```

Use `instanceof` before downcasting to avoid `ClassCastException`:

```java
if (a instanceof Dog dog) {
    dog.bark();
}
```

---

## Polymorphic Collections

```java
List<Animal> animals = new ArrayList<>();
animals.add(new Dog("Rex",   "Lab"));
animals.add(new Cat("Whiskers"));
animals.add(new Bird("Tweety"));

for (Animal animal : animals) {
    animal.makeSound(); // each responds differently
}
```

---

## Virtual Method Table (vtable)

Java uses a **vtable** internally to dispatch method calls at runtime. Every class gets a vtable with pointers to the actual method implementations — that's how dynamic dispatch works.

---

## Benefits

- Write generic code that works with many types.
- Add new types without modifying existing code (Open/Closed Principle).
- Cleaner, more readable code.

---

## References

- Liskov, B., & Wing, J. M. (1994). A behavioral notion of subtyping. *ACM TOPLAS*, 16(6), 1811–1841.
