from datetime import datetime
date_string="%d %b %Y"
date_input=input() #
date_object=datetime.strptime(date_input,date_string)
day=date_object.strftime("%A")
print(day

      
