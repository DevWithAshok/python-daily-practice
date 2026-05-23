N=int(input()) #5
for num in range(N):
    print((" "*(num))+("* "*(N-num))+(" "*(num)))
for num in range(2,N+1):
    print((" "*(N-num))+("* "*(num))+(" "*(N-num)))
