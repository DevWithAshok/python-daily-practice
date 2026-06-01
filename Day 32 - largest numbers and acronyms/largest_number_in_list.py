M=input().split(" ") #1 0 3 2 9 8
maximum=int(M[0])
for i in M:
    if int(i)>maximum:
        maximum=int(i)
print(maximum)
