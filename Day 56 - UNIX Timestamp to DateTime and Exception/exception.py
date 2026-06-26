try:
    A,B=input().split() # 0 5
    A=int(A)
    B=int(B)
    print(A/B)
except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")
