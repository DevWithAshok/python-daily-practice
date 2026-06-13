num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_list=input().split() #2 3 4
new_list=[]
for i in num_list:
    new_list+=[int(i)]
new_set=set(new_list)
if num_set.issuperset(new_set):
    print("Superset")
elif num_set.issubset(new_set):
    print("Subset")
else:
    print("Disjoint Set")
