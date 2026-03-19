# Challenge 02 – Bank System ⭐⭐

## Description

Design a small bank system using proper **encapsulation**. No field should be accessible directly from outside its class.

---

## Requirements

### Class: `BankAccount`

| Member | Details |
|--------|---------|
| `accountNumber` | `String`, read-only after construction |
| `owner` | `String`, read-only after construction |
| `balance` | `double`, never negative |
| `deposit(amount)` | Adds funds; rejects non-positive amounts |
| `withdraw(amount)` | Deducts funds; rejects if insufficient balance |
| `transfer(amount, target)` | Moves funds from this account to `target` |
| `getStatement()` | Returns a formatted string with account info |

### Class: `Bank`

| Member | Details |
|--------|---------|
| `name` | Bank name |
| `openAccount(owner)` | Creates a new `BankAccount` with an auto-generated number, adds it to internal list |
| `findAccount(accountNumber)` | Returns the matching `BankAccount` or `null` |
| `getTotalDeposits()` | Sum of all account balances |
| `printAllAccounts()` | Prints a statement for every account |

### Class: `BankDemo`

- Open a bank with at least **3 accounts**.
- Perform deposits, withdrawals, and a transfer.
- Print all accounts at the end.

---

## Expected Output (Example)

```
=== Sunrise Bank ===
ACC-001 | Alice   | Balance: $1,500.00
ACC-002 | Bob     | Balance:   $800.00
ACC-003 | Carol   | Balance: $2,200.00
Total deposits: $4,500.00
```

---

## Hints

- Use `String.format` or `printf` for currency formatting.
- Use `ArrayList<BankAccount>` in the `Bank` class.
- Generate account numbers like `"ACC-001"`, `"ACC-002"`, etc., using a static counter.
