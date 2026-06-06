list_a = input().split(",") #2,4,1,3,5
list_x = []
for num in list_a:
    list_x += [int(num)**2]
print(sorted(list_x))
