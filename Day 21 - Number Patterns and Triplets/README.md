# Day 21 - Nested Loops and Number Patterns

## Topic

Using nested loops for number patterns and mathematical logic

## Code

```python id="k8t3kp"
S = int(input())
N = int(input())

number = S

for row in range(1, N + 1):

    string = ""

    for col in range(row):
        string = string + str(number) + " "
        number = number + 1

    print(string)

N = int(input())

count = 0

for num in range(1, N + 1):

    for i in range(2, N + 1):

        for j in range(3, N + 1):

            if (num < i < j) and (num ** 2 + i ** 2 == j ** 2):
                count = count + 1

print(count)

S = int(input())
N = int(input())

count = 0

for num in range(1, N + 1):
    count = count + num

count = count + S - 1

number = N + 1

for i in range(1, N + 1):

    string = ""

    for j in range(1, number):

        string = string + str(count) + " "
        count = count - 1

    print(string)

    number = number - 1
```

## Explanation

This program demonstrates:

* Number patterns using nested loops
* Counting Pythagorean triplets
* Inverted number triangle patterns

## Key Concepts

### Nested Loops

Loops inside loops for multi-level iteration.

### Pythagorean Triplets

Triplets satisfying:
a² + b² = c²

### Pattern Printing

Combining loops and counters for structured output.

## Learning Outcome

* Practiced nested loops
* Learned mathematical condition checking
* Improved pattern printing logic
