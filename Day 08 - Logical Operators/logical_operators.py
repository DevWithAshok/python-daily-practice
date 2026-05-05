A=int(input())
result=(A>25)and(A<75)
print(result)


A=int(input())
S=input()
result_1=(A>12 and A<60) or (S=="yes")
print(result_1 )


M=int(input())
P=int(input())
C=int(input())
result=(M>=70 and P>=60 and C>=60) or ((M+P+C)>=180)
print(result)
