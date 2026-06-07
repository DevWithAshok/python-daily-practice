N=input().split(",") #2,5,10,15,25,30
lis_t=[]
for i in N:
    lis_t+=[int(i)]
print((sum(lis_t))/len(N))
