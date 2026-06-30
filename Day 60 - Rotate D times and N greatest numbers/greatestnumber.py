list_a = [5, 20, 3, 7, 6, 8]
k = int(input()) #2
list_len = len(list_a)
ordered_list=sorted(list_a)
result=ordered_list[len(ordered_list)-k:]
final=""
for i in result:
    final+=str(i)+" "
print(final)
