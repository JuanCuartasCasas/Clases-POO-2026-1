"""
bank_account.py

Class 03 – Encapsulation

Demonstrates:
  - Private attributes (name-mangled with __)
  - Public getters (properties) and controlled mutators
  - Validation logic inside methods
  - Read-only attribute via property without setter
"""


class BankAccount:
    """A bank account with controlled access to balance."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__owner             = owner          # private
        self.__balance           = initial_balance  # private
        self.__transaction_count = 0               # private

    # ── Read-only properties ─────────────────────────────────────────────────

    @property
    def owner(self) -> str:
        return self.__owner

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def transaction_count(self) -> int:
        return self.__transaction_count

    # ── Controlled mutators ───────────────────────────────────────────────────

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        self.__transaction_count += 1
        print(f"Deposited ${amount:,.2f}. New balance: ${self.__balance:,.2f}")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__balance:
            print("Insufficient funds.")
            return False
        self.__balance -= amount
        self.__transaction_count += 1
        print(f"Withdrew ${amount:,.2f}. New balance: ${self.__balance:,.2f}")
        return True

    def __str__(self) -> str:
        return (
            f"Account[owner={self.__owner}, "
            f"balance=${self.__balance:,.2f}, "
            f"transactions={self.__transaction_count}]"
        )


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    account = BankAccount("Alice", 1_000.00)
    print(account)

    account.deposit(500.00)
    account.withdraw(200.00)
    account.withdraw(2_000.00)   # should fail

    print(account)

    # Direct access to __balance is blocked by name mangling
    # account.__balance = 999  # This would create a NEW attribute, NOT modify the private one
