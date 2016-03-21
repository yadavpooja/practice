def squirrel(temp,summer):
    if 60 <= temp <= 90 and not summer:
        return True
    elif 60 <= temp <= 100 and summer:
        return True
    return False


print squirrel(70,False)
print squirrel(95,False)
print squirrel(95,True)
