# Number Diamond
N = int(input())
number = 1
new_number = 1
for num in range(1, 2 * N):
    string = ""
    if num <= N:
        for i in range(1, number + 1):
            string = string + str(i) + " "
        print((" " * int(N - i)) + string)
        number = number + 1
    if num > N:
        for j in range(1, N - new_number + 1):
            string = string + str(j) + " "
        print((" " * new_number) + string)
        new_number = new_number + 1


# Armstrong Numbers Between Two Intervals
M=int(input())
N=int(input())
string=""
result=""
for num in range(M,N+1):
    count=0
    length=len(str(num))
    num=str(num)
    for i in range(int(length)):
        count+=int(num[i])**int(length)
        string=int(len(str(count)))
    if count==int(num):
        result=num
        print(result, end=" ")
if result=="":
    print("-1")


# Half Pyramid Number Pattern
M=int(input())
N=int(input())
number=M
for num in range(1,N+1):
    for i in range(num):
        number=number+1
new_number=number-1
for num in range(1,N+1):
    string=""
    for i in range(num):
        string=string+str(new_number)+" "
        new_number=new_number-1
    print(string)
