def is_palindrome(string):
    if string[0::]==string[::-1]:
        return True
    else:
        return False
string = input().lower() #Noon
is_true =is_palindrome(string)
print(is_true)
