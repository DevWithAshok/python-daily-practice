N=input() #25c
if N[len(N)-1]=="C":
    N=N.strip("C")
    print(str(round(float(N),2))+"C")
    fahren=((float(N)*9)/5)+32
    print(str(round(float(fahren),2))+"F")
    kelvin=float(N)+273
    print(str(round(float(kelvin),2))+"K")
elif N[len(N)-1]=="F":
    N=N.strip("F")
    celc=(float(N)-32)*5/9
    print(str(round(float(celc),2))+"C")
    print(str(round(float(N),2))+"F")
    kelvin=float(celc)+273
    print(str(round(float(kelvin),2))+"K")
elif N[len(N)-1]=="K":
    N=N.strip("K")
    celc=(float(N)-273)
    print(str(round(float(celc),2))+"C")
    fahren=(float(celc)*9/5+32)
    print(str(round(float(fahren),2))+"F")
    print(str(round(float(N),2))+"K")
else:
    print()
    
