import datetime
date_input= int(input()) #1284105682
date=datetime.datetime(1970, 1, 1)
result=date+ datetime.timedelta(seconds=date_input)
forma_t= "%Y-%m-%d %H:%M:%S"
print(result.strftime(forma_t))
