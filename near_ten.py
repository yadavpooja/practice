def near_ten(num):
    if (num % 10) <= 2:
        return True
    elif 8 <= (num % 10) <=9:
        return True
    return False



print near_ten(12)
print near_ten(17)
print near_ten(19)
