# Day 25 - Alphabet and Sandglass Patterns

## Topic

Pattern printing using alphabets and stars

## Code

```python id="k5t3kp"
N = int(input())

S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for num in range(1, N + 1):

    string = S[0] + " "

    for i in range(1, num):
        string += S[i] + " "

    print(string)

N = int(input())

for num in range(N):

    print(
        (" " * num) +
        ("* " * (N - num)) +
        (" " * num)
    )

for num in range(2, N + 1):

    print(
        (" " * (N - num)) +
        ("* " * num) +
        (" " * (N - num))
    )
```

## Explanation

This program demonstrates:

* Alphabet sequence pattern
* Sandglass star pattern
* Nested loop based printing

## Key Concepts

### String Indexing

Used to access alphabets from a string.

### Nested Loops

Used for row and column pattern generation.

### Pattern Design

Combines spaces and symbols to create shapes.

## Learning Outcome

* Practiced alphabet patterns
* Learned sandglass pattern logic
* Improved nested loop understanding
