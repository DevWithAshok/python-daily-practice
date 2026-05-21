# Pyramid Pattern
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

# Alphabets in Hollow Rectangle
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

# First Prime Number
M = int(input())

count = 0

for num in range(1, M + 1):

    N = int(input())

    if N > 1:

        is_prime = True

        for j in range(2, N):

            if N % j == 0:
                is_prime = False
                break

        if is_prime:
            count = N
            print(count)
            break
