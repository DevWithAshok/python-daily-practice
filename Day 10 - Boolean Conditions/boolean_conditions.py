A=input()
first=int(A[0])
second=int(A[1])
third=int(A[2])
result=(first==second==third)
print(result)


A=int(input())
B=int(input())
less_than=(A<20 or B<20)
greater_than=(A>30 or B>30)
print(less_than and greater_than)


M=int(input())
P=int(input())
C=int(input())
condition_1=(M>=35 and P>=35 and C>=35)
condition_2=(M+P>=90 or P+C>=90 or M+C>=90)
print(condition_1 and condition_2)
