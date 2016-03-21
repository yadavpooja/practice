def diff(n):
    if n < 21:
        return 21 - n
    else:
        return abs(n - 21)*2



print diff(19)
print diff(11)
print diff(10)
print diff(23)
