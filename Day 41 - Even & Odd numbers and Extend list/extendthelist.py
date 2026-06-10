N=int(input()) #3
#1 2 3
#6
#8 7
new_list=[]
for i in range(N):
    Q=input().split()
    new_list+=Q
new_list.sort()
print(new_list)
