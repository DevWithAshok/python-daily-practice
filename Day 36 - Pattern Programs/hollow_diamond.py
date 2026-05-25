N=int(input()) #5
Alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,N+1):
    if i==1:
        print((" "*(N-i))+(Alpha[i-1]+" ")+(" "*(N-i)))
    else:
        print((" "*(N-i))+Alpha[i-1]+(" ")*(i-1)+(" ")*(i-2)+Alpha[i-1]+(" "*(N-i)))
for i in range(N-1,0,-1):
    if i==1:
        print((" "*(N-i))+(Alpha[i-1]+" ")+(" "*(N-i)))
    else:
        print((" "*(N-i))+Alpha[i-1]+(" ")*(i-1)+(" ")*(i-2)+Alpha[i-1]+(" "*(N-i)))
