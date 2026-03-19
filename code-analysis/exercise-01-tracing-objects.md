# Exercise 01 – Tracing Objects

## Code

```java
public class TracingExercise {

    static class Counter {
        private int count;

        Counter(int initial) {
            this.count = initial;
        }

        void increment() { count++; }
        void decrement() { count--; }
        int  getCount()  { return count; }

        @Override
        public String toString() {
            return "Counter(" + count + ")";
        }
    }

    public static void main(String[] args) {
        Counter a = new Counter(0);
        Counter b = new Counter(10);
        Counter c = a;            // (*)

        a.increment();
        a.increment();
        b.decrement();
        c.increment();            // (**)

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(a == c);
    }
}
```

---

## Questions

Answer **before** running the code.

1. How many `Counter` objects are created in this program?
2. What is the output of `System.out.println(a)` after all operations?
3. What is the output of `System.out.println(b)` after all operations?
4. After line `(**)`, does `a.getCount()` equal `c.getCount()`? Why?
5. What does `a == c` print? What does this tell us about object references?

---

## Answers

> Fill in after your analysis, then verify by running the code.

1. ___
2. ___
3. ___
4. ___
5. ___

---

## Key Takeaways

- `Counter c = a;` does **not** create a new object — it copies the **reference**.
- Any mutation through `c` is visible via `a` (and vice versa) because they point to the same heap object.
- `==` compares **references**, not content.
