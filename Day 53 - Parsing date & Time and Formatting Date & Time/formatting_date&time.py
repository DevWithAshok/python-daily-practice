from datetime import datetime
date_string="%b %d %Y %I:%M %p"
date_input=input() # Jul 01 2014 02:43PM
date_object=datetime.strptime(date_input,date_string)
result=datetime.strftime(date_object,"%d/%b/%Y %H:%M:%S")
print(result)
