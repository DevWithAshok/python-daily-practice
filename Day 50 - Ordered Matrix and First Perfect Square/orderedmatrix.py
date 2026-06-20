def list_to_str(final_list):
    string=""
    for s in final_list:
        string+=str(s)+" "
    return string
M,N=map(int,input().split())
total_list=[list(map(int,input().split()))for _ in range(M)]
new_total=[]
for i in range(M):
    for j in range(N):
        new_total.append(total_list[i][j])
new_total.sort()
count=0
for k in range(M):
    final_list=[]
    for a in range(N):
        final_list+=[(new_total[count])]
        count+=1
    final_list=list_to_str(final_list)
    print(final_list)
  
  #{I am 25 years and 10 months old}
