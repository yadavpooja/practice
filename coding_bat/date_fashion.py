def date_fashion(you,date):
    n = range(0,11)
    if you >= 8 or date >= 8:
        return 2
    elif you <=2 or date <= 2:
        return 0
    return 1




print date_fashion(5,10)
print date_fashion(5,2)
print date_fashion(5,5)
