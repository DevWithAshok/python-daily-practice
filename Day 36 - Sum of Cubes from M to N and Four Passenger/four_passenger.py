def number_of_cars_needed(no_of_people):
    typ_e=no_of_people/5
    if int(typ_e)==typ_e or no_of_people<=5:
        count=typ_e
    else:
        count=typ_e+1
    print(round(count))
no_of_people = int(input()) #5
number_of_cars_needed(no_of_people)
