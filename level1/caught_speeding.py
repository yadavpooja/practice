def caught_speeding(speed, is_birthday):
    if speed <= 60 and not is_birthday:
        return 0
    elif 61 <= speed <=80 and not is_birthday:
        return 1
    elif 81 <= speed and not is_birthday:
        return 2
    elif speed <= 65 and is_birthday:
        return 0
    elif 65 <= speed <=85 and is_birthday:
        return 1
    elif  85 <= speed and is_birthday:
        return 2


print caught_speeding(60,False)
print caught_speeding(65,False)
print caught_speeding(65,True)
print caught_speeding(85,False)
