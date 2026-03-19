# Problem 01 – Library System ⭐⭐

## Context

A small university library needs software to manage its book inventory and lending operations. You must design and implement an object-oriented solution.

---

## Requirements

### Class: `Book`

| Field / Method | Details |
|----------------|---------|
| `isbn` | `String`, unique identifier, immutable |
| `title` | `String` |
| `author` | `String` |
| `isAvailable` | `boolean`, `true` by default |
| `checkOut()` | Marks book as unavailable; fails if already checked out |
| `returnBook()` | Marks book as available again |
| `toString()` | `"[ISBN] Title – Author (available/checked out)"` |

### Class: `Member`

| Field / Method | Details |
|----------------|---------|
| `memberId` | `String`, immutable |
| `name` | `String` |
| `borrowedBooks` | `List<Book>` of currently borrowed books |
| `borrow(Book b)` | Adds book to list if available; max 3 books at a time |
| `returnBook(Book b)` | Removes from list, calls `book.returnBook()` |
| `listBorrowedBooks()` | Prints all borrowed books |

### Class: `Library`

| Field / Method | Details |
|----------------|---------|
| `name` | Library name |
| `addBook(Book b)` | Adds a book to the catalogue |
| `searchByTitle(String keyword)` | Returns books whose title contains the keyword (case-insensitive) |
| `searchByAuthor(String author)` | Returns books by that author |
| `getAvailableBooks()` | Returns all available books |
| `printCatalogue()` | Prints all books |

### Class: `LibraryDemo`

- Create a library with at least **6 books** and **3 members**.
- Simulate several borrow and return operations.
- Search for books and print results.

---

## Expected Output (Example)

```
=== University Library Catalogue ===
[978-0] Effective Java – Joshua Bloch (available)
[978-1] Clean Code – Robert Martin (checked out)
...

Search results for "java":
  [978-0] Effective Java – Joshua Bloch (available)

Alice's borrowed books:
  [978-1] Clean Code – Robert Martin
```

---

## Hints

- Keep all fields `private` and use getters/setters.
- Use `ArrayList` for collections inside `Library` and `Member`.
- Use `String.toLowerCase().contains(...)` for case-insensitive search.
