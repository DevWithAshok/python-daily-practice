# Day 18 - Loops and String Processing

## Topic

Using loops for multiplication, comparisons, and string analysis

## Code

```python id="k7t3kp"
N = int(input())

for num in range(1, 11):
    print(str(N) + " x " + str(num) + " = " + str(N * num))

N = int(input())

string = 0

for num in range(1, N + 1):

    M = int(input())

    if M > string:
        string = M

print(string)

S = input()

count = 0

for num in S:

    if num in "aeiou":
        count += 1

if count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
```

## Explanation

This program demonstrates:

* Printing multiplication tables
* Finding greatest among N numbers
* Counting vowels in a string

## Key Concepts

### for Loop

Used for repeated iteration.

### Conditional Statements

Used to compare values and check conditions.

### String Traversal

Looping through each character in a string.

## Learning Outcome

* Practiced loops and conditions
* Learned string processing
* Improved logical programming skills
