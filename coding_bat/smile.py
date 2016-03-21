def monkey(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


print  monkey(True,True)
print  monkey(False,False)
print  monkey(True,False)
