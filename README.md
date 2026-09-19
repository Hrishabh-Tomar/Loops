# super30-python-loop-task-2

Practice solutions for `break`, `continue`, `else`, `range()`, `enumerate()`,
and nested loops.

Each question has its own standalone `.py` file so it can be run and
demonstrated independently.

## Q1 — Skip multiples of 5 (`q1_skip_multiples_of_5.py`)
Loop over `range(1, 101)` and use **`continue`** to skip straight to the
next iteration whenever `num % 5 == 0`, so multiples of 5 are never printed.

## Q2 — Stop at first number divisible by 7 and 11 (`q2_break_on_7_and_11.py`)
Loop over `range(1, 101)`, checking `num % 7 == 0 and num % 11 == 0`.
As soon as that's true (77), print a message and **`break`** out of the loop
immediately instead of finishing the range.

## Q3 — Search with for-else (`q3_for_else_search.py`)
Take a user-provided number and loop through a list. If a match is found,
print `"Number Found"` and `break`. The loop's **`else`** block only runs
when the loop completes *without* hitting `break`, so it prints
`"Number Not Found"` exactly when no match was found.

## Q4 — enumerate() over names (`q4_enumerate_names.py`)
Use `enumerate(names, start=1)` to get a 1-based index alongside each name
in a single pass, instead of manually tracking a counter variable.

## Q5 — Ascending star pattern (`q5_star_pattern_ascending.py`)
For `i` in `range(1, 6)`, print `"*" * i`, so the number of stars grows by
one each row.

## Q6 — Descending star pattern (`q6_star_pattern_descending.py`)
For `i` in `range(5, 0, -1)` (counting down), print `"*" * i`, so the number
of stars shrinks by one each row.

## Q7 — Multiplication tables 1–10 (`q7_multiplication_tables.py`)
**Nested loop**: outer loop picks the table (1–10), inner loop picks the
multiplier (1–10), and each combination prints `table x i = table*i`. A
blank line separates each table for readability.

## Q8 — Divisible by both 3 and 5 (`q8_divisible_by_3_and_5.py`)
Loop over `range(1, 201)` and collect every number where
`num % 3 == 0 and num % 5 == 0` into a result list, which is essentially
every multiple of 15 in that range.

## Q9 — Unique elements without set() (`q9_unique_elements_no_set.py`)
Loop through the original list and, for each number, check
`if num not in unique_numbers` before appending it. This manually filters
out duplicates using only list membership checks — no `set()` involved.

## Q10 — Count positive / negative / zero (`q10_count_pos_neg_zero.py`)
Loop through the list once, using `if / elif / else` on each number to
increment the matching counter (`positive_count`, `negative_count`,
`zero_count`).

## Q11 — Check if a number is prime (`q11_check_prime.py`)
`is_prime(n)` loops from `2` to `int(n ** 0.5) + 1`. If any value divides
`n` evenly, it's not prime. Checking only up to the square root keeps the
loop efficient. Numbers less than 2 are handled as not prime up front.

## Q12 — All primes between 1 and 100 (`q12_primes_1_to_100.py`)
Reuses the same `is_prime()` loop logic from Q11 inside a list comprehension
that filters `range(1, 101)` down to only the prime numbers.

## How to run
Each file can be run directly, e.g.:
```bash
python3 q1_skip_multiples_of_5.py
python3 q3_for_else_search.py   # prompts for a number
python3 q11_check_prime.py      # prompts for a number
```

## YouTube demo coverage
The walkthrough video demonstrates at least 5 programs live, covering:
- **break** → Q2
- **continue** → Q1
- **for-else** → Q3
- **nested loop** → Q7
- **prime-number logic** → Q11 / Q12
