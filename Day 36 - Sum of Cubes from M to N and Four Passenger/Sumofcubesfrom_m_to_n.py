def sum_of_cubes_m_to_n(m, n):
    S_um=0
    for i in range(m,n+1):
        S_um+=i**3
    print(S_um)
m = int(input()) #3
n = int(input()) #5
sum_of_cubes_m_to_n(m,n)
