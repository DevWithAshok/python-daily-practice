from datetime import datetime
year_1,year_2=input().split() #2015 2017
monday_count=0
value=range(1,13)
for year in range(int(year_1),int(year_2)):
    for month in value:
        date_object=datetime(year,month,1)
        in_to_str=date_object.strftime()
