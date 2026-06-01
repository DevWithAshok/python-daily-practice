# Day 31 - String and List Operations 

## Topic

Python programs using strings and lists.

## Programs Included

1. Reverse Letters in Words
2. First Half Numbers of List

---

## Program 1 - Reverse Letters in Words

### Description

This program reverses the letters of each word in a sentence while maintaining the original word order.

### Code

```python
S = input()

S_1 = S.split()

for i in S_1:
    print(i[::-1], end=" ")
```

### Sample Input

```
Python is easy
```

### Sample Output

```
nohtyP si ysae
```

### Concepts Used

- Strings
- split()
- String slicing
- Loops

---

## Program 2 - First Half Numbers of List

### Description

This program extracts and prints the first half of the numbers from a space-separated list. If the list length is odd, the middle element is included.

### Code

```python
M = input()

M_1 = M.split()

Length = len(M_1)

if Length % 2 == 0:
    Length = Length
else:
    Length += 1

S = []

for i in range(int(Length / 2)):
    S += [int(M_1[i])]

print(S)
```

### Sample Input

```
10 20 30 40 50
```

### Sample Output

```
[10, 20, 30]
```

### Concepts Used

- Lists
- split()
- Type conversion
- Conditional statements
- Loops

---

## Learning Outcome

- Practiced string manipulation
- Learned string slicing techniques
- Improved list handling skills
- Worked with conditional logic and loops
