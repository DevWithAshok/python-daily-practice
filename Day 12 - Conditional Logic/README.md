# Day 12 - Conditional Logic and Modulus Operations

## Topic

Using modulus operator with conditional statements

## Code

```python id="k4t8kp"
A = int(input())

result_1 = A % 4
result_2 = A % 5

if (result_1 > result_2):
    print(result_1)
else:
    print(result_2)

N = int(input())

condition_1 = (N % 9) == 0

N = str(N)

condition_2 = (
    (int(N[0]) == 9) or
    (int(N[1]) == 9)
)

if (condition_1 or condition_2):
    print("Lucky Number")
else:
    print("Unlucky Number")

A = int(input())
B = int(input())

cond_1 = (A % 3) == 0 and (B % 3) == 0
cond_2 = (A % 12) == 0 or (B % 12) == 0

if (cond_1 and cond_2):
    print("Pair")
else:
    print("Not a Pair")
```

## Explanation

This program demonstrates:

* Using modulus operator (%)
* Applying conditional logic
* Combining multiple boolean conditions

## Key Concepts

### Modulus Operator

Returns the remainder after division.

### Conditional Statements

Used for decision making based on conditions.

### Logical Operators

AND and OR combine multiple conditions.

## Learning Outcome

* Learned modulus operations
* Practiced conditional logic
* Built multi-condition programs
