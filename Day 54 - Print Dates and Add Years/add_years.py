from datetime import  datetime, timedelta
D1=input() # Jul 11 2014 
D2=input() #Jul 19 2014
st_date=datetime.strptime(D1,"%b %d %Y")
end_date=datetime.strptime(D2,"%b %d %Y")
number_of_days=(end_date- st_date).days
for i in range(number_of_days+1):
    print(st_date + timedelta(days=i))
