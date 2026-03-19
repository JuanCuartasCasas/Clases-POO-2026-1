# Challenge 03 – Animal Hierarchy ⭐⭐⭐

## Description

Build an **animal classification hierarchy** that demonstrates inheritance, method overriding, and polymorphism.

---

## Requirements

### Abstract Class: `Animal`

| Member | Details |
|--------|---------|
| `name` | `String` |
| `age` | `int` |
| `makeSound()` | **Abstract** – each animal sounds different |
| `move()` | **Abstract** – each animal moves differently |
| `eat(String food)` | Concrete – prints `"<name> eats <food>"` |
| `describe()` | Concrete – prints full info using `makeSound()` and `move()` |

### Concrete Classes

Implement at least **4 animals**: `Dog`, `Cat`, `Eagle`, `Fish`.

Each must override `makeSound()` and `move()` with realistic behaviour.

### Interface: `Trainable`

```java
interface Trainable {
    void train(String command);
    boolean canLearnTrick(String trick);
}
```

`Dog` and `Eagle` should implement `Trainable`.

### Class: `AnimalShelter`

- Maintains a `List<Animal>`.
- `admit(Animal a)` – adds an animal.
- `describeAll()` – calls `describe()` on every animal.
- `getTrainableAnimals()` – returns a filtered list of `Trainable` animals.

---

## Expected Output (Example)

```
Rex (Dog, 3) | Sound: Woof! | Move: Runs on four legs
Whiskers (Cat, 5) | Sound: Meow | Move: Walks gracefully
Sky (Eagle, 2) | Sound: Screech! | Move: Soars through the sky
Nemo (Fish, 1) | Sound: ... | Move: Swims with fins

Trainable animals: Rex, Sky
```

---

## Hints

- Use `instanceof` or `getTrainableAnimals()` to filter trainable animals.
- Override `toString()` in each class for clean output.
- Consider using a `for-each` loop with polymorphism for `describeAll()`.
