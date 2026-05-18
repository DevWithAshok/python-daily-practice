# Numbers in right angled triangle
S=int(input())
N=int(input())
number=S
for row in range(1,N+1):
    string=""
    for col in range(row):
        string=string+str(number)+" "
        number=number+1
    print(string)

# Pythagoras triplets count
N=int(input())
count=0
for num in range(1,N+1):
    triplet=""
    for i in range(2,N+1):
        for j in range(3,N+1):
            if (num<i<j) and (num**2+i**2==j**2):
                count=count+1
print(count)


# Numbers in inverted right angled triangle
S=int(input())
N=int(input())
count=0
for num in range(1,N+1):
    count=count+num
count=count+S-1
number=N+1
for i in range(1,N+1):
    string=""
    for j in range(1,number):
        string=string+str(count)+" "
        count=count-1
    print(string)
    number=number-1
