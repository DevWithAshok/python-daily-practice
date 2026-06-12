N=int(input()) #5
mult_2=[]
mult_3=[]
for i in range(1,N+1):
    mult_2+=[2*i]
    mult_3+=[3*i]
mult_2=set(mult_2)
mult_3=set(mult_3)
result_1={}
for j in mult_2:
    result_1=mult_2- mult_3
result_1=list(result_1)
result_1.sort()
result_2={}
for k in mult_3:
    result_2=(mult_2|mult_3)-(mult_2&mult_3)
result_2=list(result_2)
result_2.sort()
print(result_1)
print(result_2)
