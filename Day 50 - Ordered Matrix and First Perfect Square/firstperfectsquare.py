M=int(input())#4
N=int(input())#16
is_perfect=[]
for i in range(M,N+1):
    for j in range(i):
        if j*j==i:
            is_perfect+=[i]
            break
if len(is_perfect)==0:
    print("No Perfect Square")
else:
    print(min(is_perfect))
