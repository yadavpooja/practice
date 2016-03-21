def makes10(a, b):
    if (a or b)== 10:
        return True
    elif (a + b) == 10:
        return True
    return False


print makes10(9, 10)
print makes10(9, 9)
print makes10(1,9)
