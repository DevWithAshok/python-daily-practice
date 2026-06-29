M=list(map(int,input().split(" "))) #3 1 2 5 3 7 7
small_num=1
for i in M: 
    if small_num in M:
        small_num+=1
    else:
        small_num=small_num
print(small_num)
