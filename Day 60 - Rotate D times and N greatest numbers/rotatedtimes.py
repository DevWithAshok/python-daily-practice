def str_to_int(first_val):
    num_list=[]
    for i in first_val:
        num_list+=[int(i)]
    return num_list
first_val=input().split(",") #1,2,3,4,5
N=int(input()) # 2 
int_list=str_to_int(first_val)
rotations=N%len(int_list)
first_part=int_list[0:rotations]
second_part=int_list[rotations:]
second_part.extend(first_part)
print(second_part)
