N=input().split(",") #5,7,3,9,8,10
length=len(N)
new_list=[]
for i in N:
    new_list+=[int(i)]
new_list=(sorted(new_list))
if length%2==0:
    print(((new_list[(length//2)-1])+(new_list[(length//2)]))/2)
else:
    print((new_list[(length//2)]))
