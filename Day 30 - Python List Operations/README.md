# Day 30 - Python List Operations

## Topic

Python programs using list manipulation and filtering.

## Programs Included

1. Swap Elements in a List
2. Numbers Divisible by 5

---

## Program 1 - Swap Elements in a List

### Description

This program swaps two elements in a predefined list based on the indices provided by the user.

### Code

```python
L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

M = int(input())
N = int(input())

first = L[M]
second = L[N]

L[M] = second
L[N] = first

print(L)
```

### Sample Input

```
2
6
```

### Sample Output

```
[1, 'two', 'four', 5.09, 'Three', -558, 9, -93.7, 'six']
```

### Concepts Used

- Lists
- Indexing
- Swapping values
- User input

---

## Program 2 - Numbers Divisible by 5

### Description

This program reads N numbers and stores only those numbers that are divisible by 5 in a list.

### Code

```python
N = int(input())

lis_t = []

for i in range(N):
    M = int(input())

    if M % 5 == 0:
        lis_t += [M]

print(lis_t)
```

### Sample Input

```
3
10
7
35
```

### Sample Output

```
[10, 35]
```

### Concepts Used

- Lists
- Loops
- Conditional statements
- Modulus operator

---

## Learning Outcome

- Practiced list indexing
- Learned element swapping
- Used lists for filtering data
- Improved understanding of loops and conditions
