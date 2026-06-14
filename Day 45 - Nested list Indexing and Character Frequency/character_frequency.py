def char_count(string):
    line=string.lower()
    value=set(line)
    value.discard(" ")
    for i in sorted(value):
        print("{}: {}".format(i,line.count(i)))
string=input() #Pop up
char_count(string)
