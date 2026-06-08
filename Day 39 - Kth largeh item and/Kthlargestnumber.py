N=input().split(",") #2,3,-1,5
new_list=N[0]
for i in N:
    if int(i)>int(new_list):
        new_list=int(i)
    else:
        new_list=new_list
print((new_list))
