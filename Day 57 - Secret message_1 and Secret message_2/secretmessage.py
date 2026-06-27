string=input() #python
string=string.lower()
mirror_dict={"a":"z","b":"y","c":"y","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q" ,"k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}
result=str()
for i in string:
    result+=mirror_dict[i]
print(result)
