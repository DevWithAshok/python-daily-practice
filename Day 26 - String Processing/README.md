# Day 26 - String Processing and Character Manipulation

## Topic

Processing strings and replacing characters

## Code

```python id="k7t3kp"
S = input()

final = "z"
initial = "a"

word = ""

for i in range(len(S)):

    value = S[i]

    if value != " ":
        word += value

    if value == " " or i == len(S) - 1:

        if word.lower() < final.lower():
            final = word

        if word.lower() > initial.lower():
            initial = word

        word = ""

final_initial = final + " " + initial

print(final_initial)

S = input()

for i in S:

    if i != " ":
        print(chr(ord(i) + 1), end="")

    else:
        print(i, end="")
```

## Explanation

This program demonstrates:

* Finding words in dictionary order
* Character replacement using ASCII values
* String traversal and manipulation

## Key Concepts

### lower()

Used for case-insensitive string comparison.

### ord()

Returns ASCII value of a character.

### chr()

Converts ASCII value back to character.

## Learning Outcome

* Practiced string processing
* Learned ASCII character manipulation
* Improved logical thinking with strings
