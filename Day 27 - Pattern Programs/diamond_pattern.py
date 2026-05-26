N=int(input()) #5
for i in range(1,N):
    if i==1:
        print((". "*(N-i))+"0 "+(". "*(N-i)))
    else:
        print((". "*(N-i))+"0 "*(2*i-1)+(". "*(N-i)))
for i in range(N,0,-1):
    if i==1:
        print((". "*(N-i))+"0 "+(". "*(N-i)))
    else:
        print((". "*(N-i))+"0 "*(2*i-1)+(". "*(N-i)))
