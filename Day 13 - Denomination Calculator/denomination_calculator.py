A=int(input()) # Denominations using 16
five_r=A/5
five_r=str(int(five_r))
one_r=(A-(int(five_r)*5))
one_r=str(int(one_r))
print("5:" +(five_r))
print("1:" +(one_r))


A=int(input()) # Denominations using 1543
fivehund_r=A/500
cond_1=int(fivehund_r)
fifty_r=A-(cond_1*500)
cond_2=fifty_r/50
ten_r=fifty_r-(int(cond_2)*50)
cond_3=ten_r/10
one_r=ten_r-(int(cond_3)*10)
cond_4=one_r/1
print("500: "+ str(cond_1)+" "+"50: "+str(int(cond_2))+" " + "10: "+str(int(cond_3))+" "+"1: "+str(int(cond_4)))
