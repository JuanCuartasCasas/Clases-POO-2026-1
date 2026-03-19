# Challenge 01 – Student Class ⭐

## Description

Create a class that models a **university student** in Python.

---

## Requirements

### Class: `Student`

| Member | Type | Details |
|--------|------|---------|
| `student_id` | `str` | Unique identifier, e.g. `"2026-001"` |
| `first_name` | `str` | Student's first name |
| `last_name` | `str` | Student's last name |
| `__grades` | `list[float]` | Private — grades recorded so far |
| `full_name` | property | Returns `"FirstName LastName"` |
| `gpa` | property | Average of all recorded grades (0.0 if none) |
| `record_grade(grade)` | method | Validates range [0.0, 5.0] then appends |
| `is_honor_roll()` | method | Returns `True` if `gpa >= 4.5` |
| `__str__` | dunder | Readable summary |

### Script

Create at least **3 student objects**, record several grades for each, and print their information.

---

## Expected Output (Example)

```
Student[id=2026-001, name=Alice Smith, gpa=4.80] -> Honor Roll: True
Student[id=2026-002, name=Bob Johnson, gpa=3.60] -> Honor Roll: False
Student[id=2026-003, name=Carol White, gpa=4.50] -> Honor Roll: True
```

---

## Hints

- Use a private list `self.__grades = []` to store grades.
- The `gpa` property computes `sum(self.__grades) / len(self.__grades)`.
- Validate that grades are in the range [0.0, 5.0] before appending.
- Use `@property` instead of explicit getter methods.

