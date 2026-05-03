A=int(input())
Area=A*A
print("Area of the square is: " + str(Area) )
Peri=4*A
print("Perimeter of the square is: " + str(Peri))

w1=input()
result=len(w1)-2
print(w1[2:result])

W=input()
I_1=int(input())
C=input()
result=W[:I_1]+C+W[(I_1+1):]
print(result)
