# Day 13 - Currency Denomination Calculator

## Topic

Calculating currency denominations using arithmetic operations

## Code

```python id="k7t3kp"
A = int(input())

five_r = A / 5
five_r = str(int(five_r))

one_r = (A - (int(five_r) * 5))
one_r = str(int(one_r))

print("5:" + five_r)
print("1:" + one_r)

A = int(input())

fivehund_r = A / 500
cond_1 = int(fivehund_r)

fifty_r = A - (cond_1 * 500)

cond_2 = fifty_r / 50

ten_r = fifty_r - (int(cond_2) * 50)

cond_3 = ten_r / 10

one_r = ten_r - (int(cond_3) * 10)

cond_4 = one_r / 1

print(
    "500: " + str(cond_1) + " " +
    "50: " + str(int(cond_2)) + " " +
    "10: " + str(int(cond_3)) + " " +
    "1: " + str(int(cond_4))
)
```

## Explanation

This program demonstrates:

* Breaking amount into denominations
* Using arithmetic operations
* Applying integer conversion

## Example Inputs

### Input 1

16

Output:
5:3
1:1

### Input 2

1543

Output:
500: 3 50: 0 10: 4 1: 3

## Key Concepts

### Division

Used to calculate number of notes.

### Modulus-like Logic

Remaining amount is calculated after denomination extraction.

### Type Conversion

int() converts decimal values to integers.

## Learning Outcome

* Learned denomination calculation
* Practiced arithmetic operations
* Improved problem-solving logic
