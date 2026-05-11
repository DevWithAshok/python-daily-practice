# Day 14 - Loops and Calculations

## Topic

Using while loop and for loop for calculations

## Code

```python
N = int(input())

counter = 0
product = 1

while counter < N:
    M = int(input())
    product = product * M
    M = M + 1
    counter = counter + 1

print(product)

N = int(input())

count = 0
sum = 0

for num in range(1, N + 1):
    sum = sum + num
    count = count + 1

avg = sum / count

print(avg)
```

## Explanation

This program demonstrates:

* Using while loop
* Using for loop
* Calculating product and average

## Key Concepts

### while Loop

Executes repeatedly while condition is True.

### for Loop

Iterates through a sequence of values.

### range()

Generates sequence of numbers.

## Learning Outcome

* Learned while loop
* Learned for loop
* Practiced iterative calculations
