/**
 * BankAccount.java
 *
 * Class 03 – Encapsulation
 *
 * Demonstrates:
 *   - Private fields protected from direct access
 *   - Public getters and controlled mutators
 *   - Validation logic inside methods
 *   - Immutable helper value object (Money)
 */
public class BankAccount {

    private final String owner;
    private double balance;
    private int    transactionCount;

    public BankAccount(String owner, double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative.");
        }
        this.owner            = owner;
        this.balance          = initialBalance;
        this.transactionCount = 0;
    }

    // --- Getters (read-only access) ---
    public String getOwner()            { return owner; }
    public double getBalance()          { return balance; }
    public int    getTransactionCount() { return transactionCount; }

    // --- Controlled mutators ---
    public void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Deposit amount must be positive.");
            return;
        }
        balance += amount;
        transactionCount++;
        System.out.printf("Deposited $%.2f. New balance: $%.2f%n", amount, balance);
    }

    public boolean withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Withdrawal amount must be positive.");
            return false;
        }
        if (amount > balance) {
            System.out.println("Insufficient funds.");
            return false;
        }
        balance -= amount;
        transactionCount++;
        System.out.printf("Withdrew $%.2f. New balance: $%.2f%n", amount, balance);
        return true;
    }

    @Override
    public String toString() {
        return String.format("Account[owner=%s, balance=%.2f, tx=%d]",
                owner, balance, transactionCount);
    }

    // ----- Demo -----
    public static void main(String[] args) {
        BankAccount account = new BankAccount("Alice", 1_000.00);
        System.out.println(account);

        account.deposit(500.00);
        account.withdraw(200.00);
        account.withdraw(2_000.00); // should fail

        System.out.println(account);
    }
}
