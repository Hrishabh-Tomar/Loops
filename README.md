# super30-python-loop-task-2

Practice solutions for `break`, `continue`, `else`, `range()`, `enumerate()`,
and nested loops — all implemented in a single Jupyter notebook,
**`Intermediate_loops.ipynb`**.

## How to run
1. Clone this repository.
2. Open `Intermediate_loops.ipynb` in Jupyter Notebook, JupyterLab, or
   VS Code (with the Jupyter extension).
3. Run the cells from top to bottom (Cell → Run All, or run each cell with
   Shift+Enter). Cells for Q3 and Q11 will prompt for input — type a value
   and press Enter to continue.

Each question has its own labeled cell (with a markdown header, e.g.
"Q3: Search for a user-provided number inside a list using for-else"),
so you can scroll to the one you want or run them individually.

## Question-by-question approach

### Q1 — Skip multiples of 5
Loop over `range(1, 101)` and use **`continue`** to skip straight to the
next iteration whenever `num % 5 == 0`.

### Q2 — Stop at first number divisible by 7 and 11
Loop over `range(1, 101)`, checking `num % 7 == 0 and num % 11 == 0`.
As soon as that's true (77), print a message and **`break`** immediately.

### Q3 — Search with for-else
Loop through a list looking for a user-provided number. If found, print
`"Number Found"` and `break`. The loop's **`else`** block runs only when
the loop finishes without hitting `break`, printing `"Number Not Found"`.

### Q4 — enumerate() over names
Use `enumerate(names, start=1)` to get a 1-based index alongside each name.

### Q5 / Q6 — Star patterns
Ascending: `"*" * i` for `i` in `range(1, 6)`.
Descending: `"*" * i` for `i` in `range(5, 0, -1)`.

### Q7 — Multiplication tables 1–10
**Nested loop**: outer loop picks the table, inner loop picks the
multiplier, printing `table x i = table*i` for each combination.

### Q8 — Divisible by both 3 and 5
Loop over `range(1, 201)` and collect numbers where
`num % 3 == 0 and num % 5 == 0`.

### Q9 — Unique elements without set()
Loop through the list and append to a new list only if
`num not in unique_numbers`.

### Q10 — Count positive / negative / zero
Loop through the list once, using `if / elif / else` to increment the
matching counter.

### Q11 — Check if a number is prime
Loop from `2` to `int(n ** 0.5) + 1`; if any value divides `n` evenly,
it's not prime.

### Q12 — All primes between 1 and 100
Reuses the Q11 prime-check loop in a list comprehension over `range(1, 101)`.

## YouTube demo coverage
The walkthrough video demonstrates at least 5 programs live, covering:
- **break** → Q2
- **continue** → Q1
- **for-else** → Q3
- **nested loop** → Q7
- **prime-number logic** → Q11 / Q12
