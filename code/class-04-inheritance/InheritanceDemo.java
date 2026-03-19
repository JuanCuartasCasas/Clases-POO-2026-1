/**
 * Animal.java  /  Dog.java  /  Cat.java  /  InheritanceDemo.java
 *
 * Class 04 – Inheritance
 *
 * Demonstrates:
 *   - Parent class with protected fields
 *   - Child classes using `extends` and `super`
 *   - Method overriding with @Override
 *   - Calling a superclass method from a subclass
 */

// ===================== Parent class =====================
class Animal {
    protected String name;
    protected int    age;

    public Animal(String name, int age) {
        this.name = name;
        this.age  = age;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }

    public void sleep() {
        System.out.println(name + " is sleeping.");
    }

    @Override
    public String toString() {
        return "Animal[name=" + name + ", age=" + age + "]";
    }
}

// ===================== Dog (child) =====================
class Dog extends Animal {
    private String breed;

    public Dog(String name, int age, String breed) {
        super(name, age);    // call Animal constructor
        this.breed = breed;
    }

    public void bark() {
        System.out.println(name + " says: Woof!");
    }

    @Override
    public void eat() {
        super.eat();         // reuse parent behaviour …
        System.out.println(name + " wags its tail while eating.");  // … then extend it
    }

    @Override
    public String toString() {
        return "Dog[name=" + name + ", age=" + age + ", breed=" + breed + "]";
    }
}

// ===================== Cat (child) =====================
class Cat extends Animal {
    private boolean isIndoor;

    public Cat(String name, int age, boolean isIndoor) {
        super(name, age);
        this.isIndoor = isIndoor;
    }

    public void purr() {
        System.out.println(name + " purrs contentedly.");
    }

    @Override
    public void eat() {
        System.out.println(name + " eats very delicately.");
    }

    @Override
    public String toString() {
        return "Cat[name=" + name + ", age=" + age + ", indoor=" + isIndoor + "]";
    }
}

// ===================== Demo =====================
public class InheritanceDemo {
    public static void main(String[] args) {
        Dog dog = new Dog("Rex",      3, "Labrador");
        Cat cat = new Cat("Whiskers", 5, true);

        System.out.println(dog);
        dog.eat();
        dog.bark();
        dog.sleep();

        System.out.println();

        System.out.println(cat);
        cat.eat();
        cat.purr();
        cat.sleep();
    }
}
