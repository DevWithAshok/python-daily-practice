# Day 24 - Advanced Patterns and Prime Numbers

## Topic

Pattern printing with alphabets and prime number checking

## Code

```python id="k9t3kp"
N = int(input())

number = 1

for num in range(1, N + 1):

    string = ""

    for i in range(1, num + 1):
        string = "0 " * number

    print(
        (". " * (N - num)) +
        string +
        (". " * (N - num))
    )

    number += 2

M = int(input())
N = int(input())

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = 0

for num in range(1, M + 1):

    string = ""

    for i in range(1, N + 1):

        if num == 1 or num == M:
            print(letters[number], end=" ")
            number += 1

        elif i == 1 or i == N:
            string += letters[number] + " "
            number += 1

        else:
            string += "  "
            number += 1

    print(string)

M = int(input())

for num in range(1, M + 1):

    N = int(input())

    if N > 1:

        is_prime = True

        for j in range(2, N):

            if N % j == 0:
                is_prime = False
                break

        if is_prime:
            print(N)
            break
```

## Explanation

This program demonstrates:

* Pyramid pattern generation
* Hollow rectangle using alphabets
* Prime number checking

## Key Concepts

### Pattern Printing

Uses nested loops and spacing logic.

### Hollow Shapes

Prints only border elements while keeping inner area empty.

### Prime Number

A number greater than 1 having only two factors:
1 and itself.

## Learning Outcome

* Practiced advanced pattern logic
* Learned alphabet pattern generation
* Implemented prime number checking
