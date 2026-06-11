Q=input().split() #3 8 5 7 1 6
even_num=[]
odd_num=[]
for i in Q:
    if int(i)%2==0:
        even_num+=[int(i)]
    else:
        odd_num+=[int(i)]
even_num.sort()
print(even_num)
odd_num.sort()
print(odd_num)
