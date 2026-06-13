N=input().split() #1 2 3 5 6 7
N_int=[]
for i in N:
    N_int+=[int(i)]
misiing_num=[]
for j in range(1,N_int[len(N)-1]):
    if j in N_int:
        continue
    else:
        misiing_num+=[j]
print(misiing_num)
