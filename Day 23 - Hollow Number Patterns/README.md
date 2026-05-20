# Day 23 - Hollow Number Patterns

## Topic

Using nested loops for hollow number patterns

## Code

```python id="k7t3kp"
S = int(input())
N = int(input())

number = S - 1

for num in range(1, N + 1):

    for new_num in range(1, num + 1):
        number += 1

for i in range(N, 0, -1):

    string = ""

    if i <= 2 or i == N:

        for j in range(1, i + 1):
            string += str(number) + " "
            number -= 1

        print(("  " * (N - i)) + string)

    else:

        for k in range(1, i + 1):

            if k == 1 or k == i:
                string += str(number) + " "
                number -= 1

            else:
                string += "  "
                number -= 1

        print(("  " * (N - i)) + string)

S = int(input())
N = int(input())

number = S

for num in range(N, 0, -1):

    string = ""

    if num <= 2 or num == N:

        for i in range(1, num + 1):
            string += str(number) + " "
            number += 1

        print((" " * (N - num)) + string)

    else:

        for j in range(1, num + 1):

            if j == 1 or j == num:
                string += str(number) + " "
                number += 1

            else:
                string += "  "
                number += 1

        print((" " * (N - num)) + string)
```

## Explanation

This program demonstrates:

* Hollow right angled triangle pattern
* Hollow pyramid number pattern
* Nested loop pattern generation

## Key Concepts

### Nested Loops

Used for row and column based pattern printing.

### Hollow Patterns

Only border elements are printed while inner spaces remain empty.

### Number Manipulation

Numbers are incremented and decremented dynamically during pattern generation.

## Learning Outcome

* Practiced advanced nested loops
* Learned hollow pattern logic
* Improved number pattern programming
