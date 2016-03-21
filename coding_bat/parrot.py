def parrot(talking, hour):
    if hour < 24:
        if talking and hour < 7:
            return True
        elif talking and hour > 20:
            return True
        else:
            return False


print parrot(True,6)
print parrot(True,7)
print parrot(False,6)
print parrot(True,10)
