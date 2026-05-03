# Day 06 - Type Conversion and String Manipulation

## Topic

Using type conversion, slicing, and string replacement

## Code

```python
A = int(input())
Area = A * A
print("Area of the square is: " + str(Area))

Peri = 4 * A
print("Perimeter of the square is: " + str(Peri))

w1 = input()
result = len(w1) - 2
print(w1[2:result])

W = input()
I_1 = int(input())
C = input()

result = W[:I_1] + C + W[(I_1 + 1):]
print(result)
```

## Explanation

This program demonstrates:

* Converting input to integer using int()
* Performing mathematical calculations
* Extracting substring using slicing
* Replacing a character in a string

## Key Concepts

### Type Conversion

int() converts input string to integer
str() converts number to string

### String Slicing

Used to extract or modify parts of a string

### String Replacement Logic

Replaces character at a specific index

## Learning Outcome

* Learned type conversion
* Practiced string slicing
* Implemented character replacement
* Combined multiple concepts
