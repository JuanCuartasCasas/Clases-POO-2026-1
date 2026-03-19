/**
 * Car.java
 *
 * Class 02 – Classes and Objects
 *
 * Demonstrates:
 *   - Defining a class with private fields
 *   - Multiple constructors (overloading)
 *   - The `this` keyword
 *   - A toString() override
 */
public class Car {

    // Fields
    private String brand;
    private String model;
    private int    year;
    private double price;

    // Default constructor
    public Car() {
        this("Unknown", "Unknown", 0, 0.0);
    }

    // Parameterised constructor
    public Car(String brand, String model, int year, double price) {
        this.brand = brand;
        this.model = model;
        this.year  = year;
        this.price = price;
    }

    // Getters
    public String getBrand() { return brand; }
    public String getModel() { return model; }
    public int    getYear()  { return year;  }
    public double getPrice() { return price; }

    // Behaviour
    public void displayInfo() {
        System.out.println(this); // calls toString()
    }

    @Override
    public String toString() {
        return year + " " + brand + " " + model + " – $" + String.format("%.2f", price);
    }

    // ----- Demo -----
    public static void main(String[] args) {
        Car car1 = new Car("Toyota", "Corolla", 2024, 22_000.00);
        Car car2 = new Car("Honda",  "Civic",   2023, 20_500.00);
        Car car3 = new Car(); // default values

        car1.displayInfo();
        car2.displayInfo();
        car3.displayInfo();

        // Identity vs Equality
        Car carA = new Car("Toyota", "Corolla", 2024, 22_000.00);
        System.out.println("car1 == carA  : " + (car1 == carA));           // false (different refs)
        System.out.println("car1.equals(carA): " + car1.equals(carA));     // false (no equals override)
    }
}
