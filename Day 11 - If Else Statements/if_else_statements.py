A=int(input())
if (A<0):
    A=A*(-1)
    print(A)
else:
    print(A)

X=int(input())
Y=int(input())
if (X<Y):
    print("X < Y")
else:
    print("X >= Y")

A=int(input())
B=int(input())
C=int(input())
result=((A+B)>C and (B+C)>A and (A+C)>B)
if (result):
    print("It's a Triangle")
else:
    print("It's not a Triangle")
