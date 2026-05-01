# Day 05 - String Manipulation and Patterns

## Topic

String modification, length operations, and pattern printing

## Code

```python id="h9t3kp"
word = input()
letter = (len(word) - 1) * "*"
print(word[0] + letter)

print(len(input()) - 2)

print("* " * 2)
print("* " * 2)
print("* " * 2)
```

## Explanation

This program demonstrates:

* Replacing characters in a string
* Performing calculations using string length
* Printing simple patterns

## Key Concepts

### String Replacement Logic

Keeps the first character and replaces remaining characters with `*`.

### len()

Used to calculate string length.

### String Multiplication

Used to print repeated patterns.

## Example

Input:
Hello

Output:
H****

## Learning Outcome

* Learned string manipulation
* Practiced length-based logic
* Printed basic patterns
