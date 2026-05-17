# Hollow rectangle
M=int(input())
N=int(input())
rows=M+2
columns=N+2
for num in range(1,rows+1):
    if (num==1):
        print("+"+("-"*N)+"+")
    elif(num==rows):
        print("+"+("-"*N)+"+")
    else:
        print("|"+(" "*N)+"|")


# Inverted right angle triangle
N=int(input())
spaces=0
stars=0
for i in range(0,N):
    spaces="  "*(2*i)
    stars="* "*((2*(N-i))-1)
    print(spaces+stars)

# Sum of even numbers
N=int(input())
sum=0
for num in range(0,N+1):
    if num%2==0:
        sum=sum+num
    else:
        sum=sum
print(sum)
