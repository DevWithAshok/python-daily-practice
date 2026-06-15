def get_principal_diagonal_elements(matrix, m, n):
    diagonal_list=[]
    for i in range(n):
        diagonal_list+=[matrix[i][i]]
    print(diagonal_list)
def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list
m, n = input().split() 3 3
# 1 2 3
# 10 20 30
# 5 10 15
m, n = int(m), int(n)
num_list = []
for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
get_principal_diagonal_elements(num_list,m,n)
