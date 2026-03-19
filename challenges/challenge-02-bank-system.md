# Challenge 02 – Bank System ⭐⭐

## Description

Design a small bank system using proper **encapsulation**. No private attribute should be accessible directly from outside its class.

---

## Requirements

### Class: `BankAccount`

| Member | Details |
|--------|---------|
| `__account_number` | `str`, read-only via `@property` |
| `__owner` | `str`, read-only via `@property` |
| `__balance` | `float`, never negative, read-only via `@property` |
| `deposit(amount)` | Adds funds; rejects non-positive amounts |
| `withdraw(amount)` | Deducts funds; returns `False` if insufficient |
| `transfer(amount, target)` | Moves funds from this account to `target` |
| `get_statement()` | Returns a formatted string with account info |

### Class: `Bank`

| Member | Details |
|--------|---------|
| `name` | Bank name |
| `open_account(owner)` | Creates a new `BankAccount` with auto-generated number, adds it to internal list |
| `find_account(account_number)` | Returns matching account or `None` |
| `total_deposits` | Property — sum of all account balances |
| `print_all_accounts()` | Prints a statement for every account |

### Script (`bank_demo.py`)

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

- Use f-strings with `{value:,.2f}` for currency formatting.
- Use a `list[BankAccount]` inside the `Bank` class.
- Generate account numbers using a class variable counter: `Bank._counter`.
- Use `@property` for `total_deposits`.

