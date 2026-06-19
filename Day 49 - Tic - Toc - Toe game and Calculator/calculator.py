N=input().split()
if N[1]=="+":
    print(int(N[0])+int(N[2]))
elif N[1]=="-":
    print(int(N[0])-int(N[2]))
elif N[1]=="*":
    print(int(N[0])*int(N[2]))
elif N[1]=="/":
    print(int(N[0])/int(N[2]))
elif N[1]=="%":
    print(int(N[0])%int(N[2]))
else:
    print()
