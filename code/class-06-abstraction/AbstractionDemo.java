/**
 * AbstractionDemo.java
 *
 * Class 06 – Abstraction
 *
 * Demonstrates:
 *   - Abstract class with abstract and concrete methods
 *   - Concrete subclasses implementing abstract behaviour
 *   - Working with abstract type references
 */

// ===================== Abstract base =====================
abstract class Vehicle {
    private String brand;
    private int    year;

    public Vehicle(String brand, int year) {
        this.brand = brand;
        this.year  = year;
    }

    // Abstract – subclass MUST define this
    public abstract void startEngine();
    public abstract int  maxSpeed();     // km/h

    // Concrete – shared behaviour
    public void displayInfo() {
        System.out.printf("%s %s (max %d km/h)%n",
                year, brand, maxSpeed());
    }

    public String getBrand() { return brand; }
    public int    getYear()  { return year;  }
}

// ===================== Car =====================
class ElectricCar extends Vehicle {
    private int batteryCapacityKwh;

    public ElectricCar(String brand, int year, int batteryCapacityKwh) {
        super(brand, year);
        this.batteryCapacityKwh = batteryCapacityKwh;
    }

    @Override
    public void startEngine() {
        System.out.println(getBrand() + ": Electric motor activated silently.");
    }

    @Override
    public int maxSpeed() { return 250; }

    public int getBatteryCapacity() { return batteryCapacityKwh; }
}

// ===================== Motorcycle =====================
class GasolineMotorcycle extends Vehicle {
    private int cylinderCc;

    public GasolineMotorcycle(String brand, int year, int cylinderCc) {
        super(brand, year);
        this.cylinderCc = cylinderCc;
    }

    @Override
    public void startEngine() {
        System.out.println(getBrand() + ": Vroom! " + cylinderCc + "cc engine started.");
    }

    @Override
    public int maxSpeed() { return 180; }
}

// ===================== Demo =====================
public class AbstractionDemo {

    public static void main(String[] args) {
        // Use abstract type as reference (abstraction in action)
        Vehicle[] fleet = {
            new ElectricCar("Tesla",  2024, 100),
            new GasolineMotorcycle("Honda", 2023, 600)
        };

        for (Vehicle v : fleet) {
            v.displayInfo();
            v.startEngine();
            System.out.println();
        }

        // Downcast to access subclass-specific behaviour
        if (fleet[0] instanceof ElectricCar ev) {
            System.out.println("Battery capacity: " + ev.getBatteryCapacity() + " kWh");
        }
    }
}
