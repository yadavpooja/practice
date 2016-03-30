def lone_sum(a,b,c):
    if a!= b and b != c and a != c:
        return a + b + c
    elif a == b and b != c :
        return b + c
    elif a != b and b == c:
        return a + b
    elif a == c and a != b:
        return b
    return 0
   # elif a == b == c:
    #    return 0
    




print lone_sum(1,2,3)
print lone_sum(3,2,3)
print lone_sum(3,3,3)

