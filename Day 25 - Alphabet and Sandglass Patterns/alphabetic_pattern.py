N=int(input()) #5
S="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for num in range(1,N+1):
    string=S[0]+" "
    for i in range(1,num):
        string+=S[i]+" "
    print(string)
