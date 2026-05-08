# Day 11 - if-else Statements in Python

## Topic

Using if-else conditions for decision making

## Code

```python
A = int(input())

if (A < 0):
    A = A * (-1)
    print(A)
else:
    print(A)

X = int(input())
Y = int(input())

if (X < Y):
    print("X < Y")
else:
    print("X >= Y")

A = int(input())
B = int(input())
C = int(input())

result = (
    (A + B) > C and
    (B + C) > A and
    (A + C) > B
)

if (result):
    print("It's a Triangle")
else:
    print("It's not a Triangle")
```

## Explanation

This program demonstrates:

* Using if-else statements
* Comparing numbers
* Validating triangle conditions

## Key Concepts

### if Statement

Executes code only if condition is True.

### else Statement

Executes alternative code when condition is False.

### Triangle Condition

A triangle is valid only if:

* Sum of any two sides is greater than the third side

## Learning Outcome

* Learned if-else statements
* Practiced conditional execution
* Built logical decision-making programs
