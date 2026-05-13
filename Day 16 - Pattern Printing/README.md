# Day 16 - Pattern Printing using Loops

## Topic

Using while loops for pattern printing

## Code

```python id="v4t8kp"
N = int(input())

counter = 0
sum = 0

while counter < N:
    sum = int(sum) + 1
    sum = str(sum)

    counter = counter + 1

    print(sum * N)

N = int(input())

counter = 0
sum = 0

while counter < N:
    sum = sum + 1

    print("*" * sum)

    counter = counter + 1

M = int(input())
N = int(input())

counter = 0

while counter < M:
    print("*" * N)

    counter = counter + 1
```

## Explanation

This program demonstrates:

* Number pattern printing
* Triangle star pattern
* Rectangle star pattern
* Using while loops for repetition

## Key Concepts

### while Loop

Repeats execution while condition is True.

### String Multiplication

Used to repeat characters and numbers.

### Pattern Printing

Common beginner programming practice for logic building.

## Learning Outcome

* Learned pattern printing
* Practiced nested repetition logic
* Improved loop understanding
