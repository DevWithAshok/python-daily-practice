# Day 08 - Logical Operators in Python

## Topic

Using AND and OR operators for decision making

## Code

```python
A = int(input())
result = (A > 25) and (A < 75)
print(result)

A = int(input())
S = input()
result_1 = (A > 12 and A < 60) or (S == "yes")
print(result_1)

M = int(input())
P = int(input())
C = int(input())

result = (M >= 70 and P >= 60 and C >= 60) or ((M + P + C) >= 180)
print(result)
```

## Explanation

This program demonstrates:

* Using logical AND and OR operators
* Combining multiple conditions
* Evaluating boolean expressions

## Key Concepts

### AND Operator

Returns True only if all conditions are True

### OR Operator

Returns True if at least one condition is True

## Learning Outcome

* Learned logical operators
* Practiced combining conditions
* Built decision-making logic
