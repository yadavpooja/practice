def neg(a, b, negative):
    if (a < 0 and b > 0) or (a > 0 and b < 0) and not negative:
        return True
    elif a and b < 0 and negative:
        return True
    else:
        return False


print neg(1, 1, False)
print neg(-1, 1, False)
print neg(-4, -5, True)

