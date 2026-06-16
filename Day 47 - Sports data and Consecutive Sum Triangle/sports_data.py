students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}
N=int(input()) #3
# Gopal Hockey
# Jyothi Cricket
# Akhil Football
for i in range(N):
    key_value=input().split()
    students_dict[key_value[0]]=key_value[1]
print(students_dict)
