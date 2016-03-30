def love6(a,b):
    if a == 6 or b == 6:
        return True
    elif abs(a - b) == 6 or abs(b - a) == 6:
        return True
    elif abs(a + b) == 6 or abs(b + a) == 6:
        return True
    return False




print love6(6,4)
print love6(5,4)
print love6(1,5)
print love6(6,12)
