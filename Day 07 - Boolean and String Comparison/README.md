# Day 07 - Boolean Expressions and String Comparison

## Topic

Using comparison operators and string slicing

## Code

```python
A = int(input())
B = int(input())

result1 = (A <= B)
print("A <= B is " + str(result1))

result2 = (B <= A)
print("B <= A is " + str(result2))

w1 = input()
w2 = int(input())

result = (w1[0:w2] != w1[len(w1) - w2:])
print(result)

s1 = input()
s2 = input()

result = (s1[:len(s2)] == s2)
print(result)
```

## Explanation

This program demonstrates:

* Comparing numbers using relational operators
* Working with boolean values
* Comparing parts of strings using slicing

## Key Concepts

### Comparison Operators

* `<=` checks less than or equal
* Returns True or False

### String Slicing

Used to extract parts of a string

### Boolean Result

Expressions return True or False

## Learning Outcome

* Learned boolean expressions
* Practiced comparisons
* Used slicing for string comparison
