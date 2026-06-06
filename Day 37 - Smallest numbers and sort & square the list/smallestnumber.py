S=input() #2,3,-1,5
S_list=S.split(",")
result=S_list[0]
for i in S_list:
    if int(result)>int(i):
        result=i
print(result)
