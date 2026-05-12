# Day 15 - Conditional Statements and Leap Year

## Topic

Using if-elif-else conditions and leap year logic

## Code

```python id="h7t3kp"
A = int(input())
B = int(input())
C = int(input())

if (A > B and A > C):
    print(A)
elif (B > A and B > C):
    print(B)
else:
    print(C)

Y = int(input())

cond_1 = (Y % 400) == 0
cond_2 = ((Y % 4) == 0 and (Y % 100) != 0)

print(cond_1 or cond_2)
```

## Explanation

This program demonstrates:

* Finding the greatest among three numbers
* Checking leap year conditions
* Using if-elif-else statements

## Key Concepts

### if-elif-else

Used for multiple conditional checks.

### Leap Year Logic

A year is a leap year if:

* Divisible by 400
  OR
* Divisible by 4 but not by 100

## Learning Outcome

* Learned if-elif-else ladder
* Practiced comparison logic
* Implemented leap year validation
