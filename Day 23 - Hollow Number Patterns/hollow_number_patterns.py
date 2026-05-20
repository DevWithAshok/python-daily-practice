# Numbers in inverted hollow right angled triangle
S=int(input()) #2
N=int(input()) #3
number=S-1
for num in range(1,N+1):
    for new_num in range(1,num+1):
        number+=1
for i in range(N,0,-1):
    string=""
    if i<=2 or i==N:
        for j in range(1,i+1):
            string+=str(number)+" "
            number-=1
        print(("  "*(N-i))+string)
    else:
        for k in range(1,i+1):
            if k==1 or k==i:
                string+=str(number)+" "
                number-=1
            else:
                string+="  "
                number-=1
        print(("  "*(N-i))+string)



# Numbers in inverted hollow pyramid
S=int(input()) #3
N=int(input()) #4
number=S
for num in range(N,0,-1):
    string=""
    if num<=2 or num==N:
        for i in range(1,num+1):
            string+=str(number)+" "
            number+=1
        print((" "*(N-num))+string)
    else:
        for j in range(1,num+1):
            if j==1 or j==num:
                string+=str(number)+" "
                number+=1
            else:
                string+="  "
                number+=1
        print((" ")*(N-num)+string)
