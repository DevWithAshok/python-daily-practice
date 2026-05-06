# Day 09 - Complex Logical Conditions in Python

## Topic

Using multiple logical conditions and string indexing

## Code

```python id="h7t3kp"
A = input()

first = int(A[0])
second = int(A[1])
third = int(A[2])

result_1 = (first > 7 and second > 7 and third > 7)

result_2 = (
    (first * second) <= 30 and
    (second * third) <= 30 and
    (first * third) <= 30
)

print(result_1 or result_2)

M = int(input())
P = int(input())
C = int(input())

rule_1 = (
    (M + P) >= 100 or
    (P + C) >= 100 or
    (M + C) >= 100
)

rule_2 = (M + P + C >= 180)

print(rule_1 and rule_2)

A = input()

first = int(A[0])
second = int(A[1])
third = int(A[2])

rule_1 = (first == 1 or second == 1 or third == 1)
rule_2 = (first + second + third) < 12
rule_3 = (third == 5)

print(rule_1 and rule_2 and rule_3)
```

## Explanation

This program demonstrates:

* Extracting digits from string input
* Converting characters into integers
* Combining multiple logical conditions
* Evaluating complex boolean expressions

## Key Concepts

### String Indexing

Accessing individual digits using indexes.

### Logical Operators

Using AND and OR to combine rules.

### Boolean Expressions

Conditions evaluate to True or False.

## Learning Outcome

* Practiced complex conditions
* Improved logical thinking
* Used indexing and type conversion together
