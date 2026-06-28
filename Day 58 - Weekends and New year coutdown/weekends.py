from datetime import timedelta, datetime
d1=input() #25 Jan 2021
d2=input() #14 Feb 2021

D1=datetime.strptime(d1,"%d %b %Y")
D2=datetime.strptime(d2,"%d %b %Y")
counter_saturday=0
counter_sunday=0
current_date=D1
while current_date<=D2:
    current_day=current_date.strftime("%A")
    if current_day=="Saturday":
        counter_saturday+=1
        current_date+=timedelta(days=1)
    elif current_day=="Sunday":
        counter_sunday+=1
        current_date+=timedelta(days=1)
    else:
        current_date+=timedelta(days=1)
print("Saturday: {}".format(counter_saturday))
print("Sunday: {}".format(counter_sunday))
