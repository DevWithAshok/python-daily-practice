S=input() #to get the Ball rolling
final="z"
initial="a"
word=""
for i in range(len(S)):
    value=S[i]
    if value!=" ":
        word+=value
    if value==" " or i==len(S)-1:
        if word.lower()<final.lower():
            final=word
        if word.lower()>initial.lower():
            initial=word
        word=""
final_initial=final+" "+initial
print(final_initial)
