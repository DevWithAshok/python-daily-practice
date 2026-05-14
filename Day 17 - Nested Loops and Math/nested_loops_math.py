N=int(input())
for num in range(1,N+1):
    if num==N:
        print("+ "*N)
    else:
        string=""
        for i in range(1,num+1):
            string+="* "
        print(string)
//right angled triangle


M=int(input())
N=int(input())
string=0
for num in range(M,N+1):
    if num%2==0:
        string+=num
print(string)
//Sum of even numbers from M to N


N=int(input())
string=1
for num in range(N,0,-1):
    string=string*num
print(string)
//Factorial
