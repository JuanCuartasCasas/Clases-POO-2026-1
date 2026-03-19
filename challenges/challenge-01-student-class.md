# Challenge 01 – Student Class ⭐

## Description

Create a class that models a **university student**.

---

## Requirements

### Class: `Student`

| Member | Type | Details |
|--------|------|---------|
| `studentId` | `String` | Unique identifier, e.g. `"2026-001"` |
| `firstName` | `String` | Student's first name |
| `lastName` | `String` | Student's last name |
| `gpa` | `double` | Grade Point Average, range 0.0 – 5.0 |
| `Student(id, firstName, lastName)` | Constructor | GPA starts at 0.0 |
| `getFullName()` | Method | Returns `"FirstName LastName"` |
| `recordGrade(double grade)` | Method | Adds a grade and recalculates GPA (simple average) |
| `isHonorRoll()` | Method | Returns `true` if GPA ≥ 4.5 |
| `toString()` | Method | Readable summary |

### Class: `Main`

Create at least **3 student objects**, record several grades for each, and print their information.

---

## Expected Output (Example)

```
Student[id=2026-001, name=Alice Smith, gpa=4.80] -> Honor Roll: true
Student[id=2026-002, name=Bob Johnson, gpa=3.60] -> Honor Roll: false
Student[id=2026-003, name=Carol White, gpa=4.50] -> Honor Roll: true
```

---

## Hints

- Use a `List<Double>` or running sum + count to calculate the GPA.
- Apply encapsulation: keep fields `private`.
- Validate that grades are in range [0.0, 5.0] before recording.
