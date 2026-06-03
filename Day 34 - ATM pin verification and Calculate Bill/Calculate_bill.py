def calculate_bill(amount):
    if amount<500:
        print(amount-((amount)*(5/100)))
    elif amount>=500 and amount<2500:
        print(amount-((amount)*(10/100)))
    else:
        print(amount-((amount)*(20/100)))
amount = int(input()) #1500
calculate_bill(amount)
