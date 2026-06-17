N=input() # 1good23morning456
str_ing=""
num=""
for i in N:
    if i.isdigit():
        num+=i
    else:
        str_ing+=i
print(str_ing+num)
