M=input() #C0d1n8
numbers=[]
for i in M:
    if i.isdigit():
        numbers+=[int(i)]
print(sum(numbers))
print(min(numbers))
print(max(numbers))
