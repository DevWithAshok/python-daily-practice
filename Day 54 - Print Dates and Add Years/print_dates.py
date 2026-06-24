from datetime import datetime, timedelta
D1=input() #Jul 11 2014
# 5
Y=int(input())
date_string="%b %d %Y"
date_object=datetime.strptime(D1,date_string)
date_object=date_object+timedelta(days=365*Y)
print(date_object)
 
