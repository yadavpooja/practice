def round_sum1(a,b,c):
    a = round_sum(a)
    b = round_sum(b)
    c = round_sum(c)
    return a + b + c


def round_sum(n):
    if n % 10 >= 5:
        return n + (10 - n % 10)
    else:
        return n - n % 10



print round_sum1(16,17,18)
print round_sum1(12,13,14)
print round_sum1(6,4,4)
print round_sum(6)
