def count_of_uppercase(word):
     count=0
     for i in word:
         if i==i.upper():
             count+=1
     print(count)
word = input() #eXpLoRe
count_of_uppercase(word)
