# Day 20 - Hollow Shapes and Number Series

## Topic

Pattern printing and sum of even numbers

## Code

```python id="k4t3kp"
M = int(input())
N = int(input())

rows = M + 2
columns = N + 2

for num in range(1, rows + 1):

    if (num == 1):
        print("+" + ("-" * N) + "+")

    elif (num == rows):
        print("+" + ("-" * N) + "+")

    else:
        print("|" + (" " * N) + "|")

N = int(input())

spaces = 0
stars = 0

for i in range(0, N):

    spaces = "  " * (2 * i)
    stars = "* " * ((2 * (N - i)) - 1)

    print(spaces + stars)

N = int(input())

sum = 0

for num in range(0, N + 1):

    if num % 2 == 0:
        sum = sum + num

print(sum)
```

## Explanation

This program demonstrates:

* Hollow rectangle pattern
* Inverted triangle pattern
* Sum of even numbers

## Key Concepts

### Pattern Printing

Uses loops, spaces, and symbols for structured output.

### Conditional Statements

Used to identify borders in hollow rectangle.

### Even Number Logic

Checks divisibility using modulus operator.

## Learning Outcome

* Practiced advanced pattern printing
* Improved loop logic
* Learned number series calculations
