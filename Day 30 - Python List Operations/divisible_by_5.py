L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

M = int(input())
N = int(input())

first = L[M]
second = L[N]

L[M] = second
L[N] = first

print(L)
#Sample Input
#2
#6
