# Problem 01 – Library System ⭐⭐

## Context

A small university library needs software to manage its book inventory and lending operations. Design and implement an object-oriented solution in Python.

---

## Requirements

### Class: `Book`

| Field / Method | Details |
|----------------|---------|
| `__isbn` | `str`, unique, immutable (read-only property) |
| `__title` | `str` |
| `__author` | `str` |
| `__is_available` | `bool`, `True` by default |
| `is_available` | `@property` |
| `check_out()` | Marks book unavailable; prints error if already out |
| `return_book()` | Marks book available again |
| `__str__` | `"[ISBN] Title – Author (available/checked out)"` |

### Class: `Member`

| Field / Method | Details |
|----------------|---------|
| `member_id` | `str`, immutable |
| `name` | `str` |
| `__borrowed` | `list[Book]`, private |
| `borrow(book)` | Appends if available and member has < 3 books |
| `return_book(book)` | Removes from list, calls `book.return_book()` |
| `list_borrowed_books()` | Prints all borrowed books |

### Class: `Library`

| Field / Method | Details |
|----------------|---------|
| `name` | Library name |
| `add_book(book)` | Adds to catalogue |
| `search_by_title(keyword)` | Case-insensitive title search |
| `search_by_author(author)` | Returns books by author |
| `available_books` | Property — list of available books |
| `print_catalogue()` | Prints all books |

### Script (`library_demo.py`)

- Create a library with at least **6 books** and **3 members**.
- Simulate several borrow and return operations.
- Search for books and print results.

---

## Expected Output (Example)

```
=== University Library Catalogue ===
[978-0] Effective Python – Brett Slatkin (available)
[978-1] Clean Code – Robert Martin (checked out)
...

Search results for "python":
  [978-0] Effective Python – Brett Slatkin (available)

Alice's borrowed books:
  [978-1] Clean Code – Robert Martin
```

---

## Hints

- Keep all private attributes hidden with `__` prefix and expose them via `@property`.
- Use list comprehensions for search methods.
- Use `keyword.lower() in book.title.lower()` for case-insensitive search.

