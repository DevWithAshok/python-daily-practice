def conv_str_to_int(N):
    new=[]
    for num in N:
        new+=[int(num)]
    return new
def cons_num(value):
    lis_t=[]
    length=len(value)-1
    for i in range(length):
        lis_t+=[value[i]+value[i+1]]
    length-=1
    return lis_t
N=input().split(",")
value=conv_str_to_int(N)
for i in range(len(N)):
    if i==0:
        print(value)
    else:
        result=cons_num(value)
        value=result
        print(result)
