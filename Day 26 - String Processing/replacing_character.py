S=input() #Hello World
for i in S:
    if i!=" ":
        print(chr(ord(i)+1),end="")
    else:
        print(i,end="")
