# Multiplication table
N=int(input())
for num in range(1,11):
    print(str(N)+" x "+str(num)+" = "+str(N*num))

# Greatest among N numbers
N=int(input())
string=0
for num in range(1,N+1):
    M=int(input())
    if M>string:
        string=(M)
print(string)

# Count vowels in a string
S=input()
count=0
for num in S:
    if num in "aeiou":
        count+=1
if count>2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
