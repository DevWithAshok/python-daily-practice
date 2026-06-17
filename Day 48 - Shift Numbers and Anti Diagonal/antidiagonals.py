M,N=map(int,input().split()) # 2 3
# 1 5 5
# 2 7 8
diag_matrix_a=[list(map(int,input().split()))for _ in range(M)]
for i in range((M+N)-1):
    new=[]
    for j in range(M):
        check=i-j
        if 0<=check<N:
            new.append(diag_matrix_a[j][check])
    print(*new)
 
