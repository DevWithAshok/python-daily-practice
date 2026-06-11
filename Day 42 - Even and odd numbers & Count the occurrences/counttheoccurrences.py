S=input().split() #1 10 1 3 3 3
S_1=[]
for k in S:
    S_1+=[int(k)]
new_list=[]
for i in S_1:
    if i in new_list:
        continue
    count=S_1.count(i)
    if count%2!=0:
        new_list.append((i))
new_list.sort()
print(new_list)
