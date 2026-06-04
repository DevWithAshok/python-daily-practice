def shuffle_string(string, indexes_list):
    shuf_string=""
    for i in indices_list:
        shuf_string+=string[int(i)]
    return shuf_string
string = input() #tonyPh
indices_list = input().split() #4 3 0 5 1 2
result = shuffle_string(string,indices_list)
print(result)
 
