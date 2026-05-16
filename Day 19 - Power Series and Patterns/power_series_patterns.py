# Sum of n terms in power series
X=int(input())
N=int(input())
count=0
for num in range(1,N+1):
    if num%2!=0:
        count=count+(X**(2*num))
    else:
        count=count-(X**(2*num))
print(count)


# Inverted right angled triangle
N=int(input())
for num in range(N,0,-1):
    print(("  "*(N-num))+str((str(num)+" ")*num))


# Inverted pyramid
N=int(input())
print("+ "*N)
for num in range(1,N):
    print((" "*num)+("* "*(N-num)))
