/**
 * HelloOOP.java
 *
 * Class 01 – Introduction to Object-Oriented Programming
 *
 * Demonstrates the most basic OOP concepts:
 *   - Defining a class with fields and a method
 *   - Creating objects (instances)
 *   - Accessing object state and behaviour
 */
public class HelloOOP {

    // ----- A minimal class -----
    static class Animal {
        // Fields (state)
        String name;
        String sound;

        // Constructor
        Animal(String name, String sound) {
            this.name  = name;
            this.sound = sound;
        }

        // Method (behaviour)
        void makeSound() {
            System.out.println(name + " says: " + sound);
        }
    }

    // ----- Entry point -----
    public static void main(String[] args) {
        // Create two objects from the same class blueprint
        Animal dog = new Animal("Rex",      "Woof");
        Animal cat = new Animal("Whiskers", "Meow");

        dog.makeSound(); // Rex says: Woof
        cat.makeSound(); // Whiskers says: Meow

        // Each object has its own independent state
        System.out.println("Dog name: " + dog.name);
        System.out.println("Cat name: " + cat.name);
    }
}
