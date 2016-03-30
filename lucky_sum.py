def lucky_sum(a,b,c):
    if a != 13 and b != 13 and c != 13:
        return a + b + c
    elif a != 13 and b == 13:
        return a
    elif a != 13 and b != 13 and c == 13:
        return a + b
    elif a == 13:
        return 0



print lucky_sum(1,2,3)
print lucky_sum(1,2,13)
print lucky_sum(1,13,3)
