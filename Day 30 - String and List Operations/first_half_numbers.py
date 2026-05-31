M=input() 
M_1=M.split()
Length=len(M_1)
if Length%2==0:
    Length=Length
else:
    Length+=1
S=[]
for i in range(int(Length/2)):
    S+=[int(M_1[i])]
print(S)
