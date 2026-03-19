/**
 * InterfacesDemo.java
 *
 * Class 07 – Interfaces
 *
 * Demonstrates:
 *   - Declaring and implementing interfaces
 *   - A class implementing multiple interfaces
 *   - Default interface methods (Java 8+)
 *   - Functional interfaces and lambdas
 *   - Using interface type as reference
 */
import java.util.ArrayList;
import java.util.List;

// ===================== Interfaces =====================
interface Drawable {
    void draw();

    default void printLabel() {
        System.out.println("[Drawable] " + getClass().getSimpleName());
    }
}

interface Resizable {
    void resize(double factor);
}

interface Colorable {
    void setColor(String color);
    String getColor();
}

// ===================== Classes =====================
class Circle2 implements Drawable, Resizable, Colorable {
    private double radius;
    private String color;

    public Circle2(double radius, String color) {
        this.radius = radius;
        this.color  = color;
    }

    @Override public void draw()   {
        System.out.printf("Drawing Circle [radius=%.1f, color=%s]%n", radius, color);
    }

    @Override public void resize(double factor) {
        radius *= factor;
        System.out.printf("Circle resized. New radius=%.1f%n", radius);
    }

    @Override public void setColor(String color) { this.color = color; }
    @Override public String getColor()           { return color; }
}

class Square implements Drawable, Resizable, Colorable {
    private double side;
    private String color;

    public Square(double side, String color) {
        this.side  = side;
        this.color = color;
    }

    @Override public void draw() {
        System.out.printf("Drawing Square [side=%.1f, color=%s]%n", side, color);
    }

    @Override public void resize(double factor) {
        side *= factor;
        System.out.printf("Square resized. New side=%.1f%n", side);
    }

    @Override public void setColor(String color) { this.color = color; }
    @Override public String getColor()           { return color; }
}

// ===================== Functional Interface =====================
@FunctionalInterface
interface Validator {
    boolean validate(String input);
}

// ===================== Demo =====================
public class InterfacesDemo {

    public static void main(String[] args) {

        // --- Using interface type as reference ---
        System.out.println("=== Drawing Shapes ===");
        List<Drawable> drawables = new ArrayList<>();
        drawables.add(new Circle2(5.0, "red"));
        drawables.add(new Square(3.0, "blue"));

        for (Drawable d : drawables) {
            d.printLabel();   // default method
            d.draw();
        }

        // --- Multiple interface usage ---
        System.out.println("\n=== Resizing Shapes ===");
        Circle2 c = new Circle2(4.0, "green");
        c.resize(2.0);
        c.setColor("yellow");
        c.draw();

        // --- Functional interface with lambda ---
        System.out.println("\n=== Validators ===");
        Validator notEmpty     = input -> !input.isEmpty();
        Validator isEmail      = input -> input.contains("@");
        Validator shortEnough  = input -> input.length() <= 20;

        String testInput = "student@university.edu";
        System.out.println("notEmpty   : " + notEmpty.validate(testInput));
        System.out.println("isEmail    : " + isEmail.validate(testInput));
        System.out.println("shortEnough: " + shortEnough.validate(testInput));
    }
}
