# Day 22 - Advanced Number Patterns and Armstrong Numbers

## Topic

Using nested loops for advanced patterns and Armstrong number checking

## Code

```python id="k5t3kp"
N = int(input())

number = 1
new_number = 1

for num in range(1, 2 * N):

    string = ""

    if num <= N:

        for i in range(1, number + 1):
            string = string + str(i) + " "

        print((" " * int(N - i)) + string)

        number = number + 1

    if num > N:

        for j in range(1, N - new_number + 1):
            string = string + str(j) + " "

        print((" " * new_number) + string)

        new_number = new_number + 1

M = int(input())
N = int(input())

result = ""

for num in range(M, N + 1):

    count = 0

    length = len(str(num))

    temp = str(num)

    for i in range(length):
        count += int(temp[i]) ** length

    if count == num:
        result = str(num)
        print(result, end=" ")

if result == "":
    print("-1")

M = int(input())
N = int(input())

number = M

for num in range(1, N + 1):

    for i in range(num):
        number = number + 1

new_number = number - 1

for num in range(1, N + 1):

    string = ""

    for i in range(num):
        string = string + str(new_number) + " "

        new_number = new_number - 1

    print(string)
```

## Explanation

This program demonstrates:

* Number diamond pattern
* Armstrong number checking
* Half pyramid number pattern

## Key Concepts

### Nested Loops

Used for multi-level iteration and pattern generation.

### Armstrong Number

A number equal to the sum of its digits raised to the power of total digits.

Example:
153 = 1³ + 5³ + 3³

### Pattern Printing

Uses counters and loops to create structured designs.

## Learning Outcome

* Practiced advanced nested loops
* Learned Armstrong number logic
* Improved number pattern programming
