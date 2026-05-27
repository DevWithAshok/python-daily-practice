N=int(input())
su_m=0
for i in range(1,N+1):
    M=int(input())
    su_m+=M
    print(round((su_m/i),3))
