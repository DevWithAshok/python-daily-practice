# Day 19 - Power Series and Pattern Printing

## Topic

Using loops for power series and pattern generation

## Code

```python id="z8t3kp"
X = int(input())
N = int(input())

count = 0

for num in range(1, N + 1):

    if num % 2 != 0:
        count = count + (X ** (2 * num))

    else:
        count = count - (X ** (2 * num))

print(count)

N = int(input())

for num in range(N, 0, -1):

    print(
        ("  " * (N - num)) +
        str((str(num) + " ") * num)
    )

N = int(input())

print("+ " * N)

for num in range(1, N):

    print(
        (" " * num) +
        ("* " * (N - num))
    )
```

## Explanation

This program demonstrates:

* Power series calculation
* Inverted triangle pattern
* Inverted pyramid pattern

## Key Concepts

### Exponent Operator

`**` is used for power calculations.

### Loop Control

Used to generate mathematical series and patterns.

### Pattern Printing

Uses spaces and symbols for structured output.

## Learning Outcome

* Learned power series logic
* Practiced reverse loops
* Improved pattern printing skills
