# Day 17 - Nested Loops and Mathematical Programs

## Topic

Using loops for patterns and mathematical calculations

## Code

```python id="h3t8kp"
N = int(input())

for num in range(1, N + 1):

    if num == N:
        print("+ " * N)

    else:
        string = ""

        for i in range(1, num + 1):
            string += "* "

        print(string)

M = int(input())
N = int(input())

string = 0

for num in range(M, N + 1):

    if num % 2 == 0:
        string += num

print(string)

N = int(input())

string = 1

for num in range(N, 0, -1):
    string = string * num

print(string)
```

## Explanation

This program demonstrates:

* Nested loops for pattern printing
* Sum of even numbers in a range
* Factorial calculation using loops

## Key Concepts

### Nested Loops

A loop inside another loop.

### range()

Used for sequence generation.

### Factorial

Product of all positive integers from 1 to N.

## Learning Outcome

* Practiced nested loops
* Learned factorial logic
* Improved mathematical programming skills
