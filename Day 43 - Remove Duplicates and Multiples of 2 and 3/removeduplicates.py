N=input().split() #5 10 15 20 10 30 15
M=[]
for i in N:
    if int(i) not in M:
        M+=[int(i)]
    else:
        continue
M.sort()
print(M)
