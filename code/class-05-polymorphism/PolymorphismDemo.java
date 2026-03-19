/**
 * PolymorphismDemo.java
 *
 * Class 05 – Polymorphism
 *
 * Demonstrates:
 *   - Runtime polymorphism (method overriding + dynamic dispatch)
 *   - Compile-time polymorphism (method overloading)
 *   - Upcasting and downcasting
 *   - Polymorphic collection iteration
 */
import java.util.ArrayList;
import java.util.List;

// ===================== Base class =====================
abstract class Shape {
    protected String color;

    public Shape(String color) { this.color = color; }

    // Each subclass MUST implement this (runtime polymorphism)
    public abstract double area();
    public abstract double perimeter();

    public void describe() {
        System.out.printf("%s [color=%s, area=%.2f, perimeter=%.2f]%n",
                getClass().getSimpleName(), color, area(), perimeter());
    }
}

// ===================== Circle =====================
class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override public double area()      { return Math.PI * radius * radius; }
    @Override public double perimeter() { return 2 * Math.PI * radius; }
}

// ===================== Rectangle =====================
class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width  = width;
        this.height = height;
    }

    @Override public double area()      { return width * height; }
    @Override public double perimeter() { return 2 * (width + height); }
}

// ===================== Triangle =====================
class Triangle extends Shape {
    private double a, b, c;   // three sides

    public Triangle(String color, double a, double b, double c) {
        super(color);
        this.a = a; this.b = b; this.c = c;
    }

    @Override public double area() {
        double s = perimeter() / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c)); // Heron's formula
    }

    @Override public double perimeter() { return a + b + c; }
}

// ===================== Overloading demo =====================
class Printer {
    public void print(int value)    { System.out.println("int: "    + value); }
    public void print(double value) { System.out.println("double: " + value); }
    public void print(String value) { System.out.println("String: " + value); }
}

// ===================== Demo =====================
public class PolymorphismDemo {

    public static void main(String[] args) {

        // --- Polymorphic collection ---
        List<Shape> shapes = new ArrayList<>();
        shapes.add(new Circle("red",    5.0));
        shapes.add(new Rectangle("blue", 4.0, 6.0));
        shapes.add(new Triangle("green", 3.0, 4.0, 5.0));

        System.out.println("=== All Shapes ===");
        for (Shape s : shapes) {
            s.describe();   // correct implementation called at runtime
        }

        // --- Upcasting / Downcasting ---
        System.out.println("\n=== Casting ===");
        Shape s = new Circle("yellow", 3.0); // upcasting
        if (s instanceof Circle c) {         // pattern matching instanceof (Java 16+)
            System.out.println("Radius available after downcast: use Circle API here");
            c.describe();
        }

        // --- Compile-time overloading ---
        System.out.println("\n=== Overloading ===");
        Printer p = new Printer();
        p.print(42);
        p.print(3.14);
        p.print("Hello OOP");
    }
}
