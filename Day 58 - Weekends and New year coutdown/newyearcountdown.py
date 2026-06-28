from datetime import datetime, timedelta
D=input() #Dec 30 2020 02:43 PM
D_object=datetime.strptime(D,"%b %d %Y %I:%M %p")
next_newyear=datetime(D_object.year +1,1,1)
diff=next_newyear- D_object

total_seconds=diff.total_seconds()

hours=int(total_seconds//3600)
minutes=int((total_seconds%3600)//60)
print("{} hours {} minutes".format(hours,minutes))
