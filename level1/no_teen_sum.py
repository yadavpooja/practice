def no_teen_sum(a,b,c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)

    return a + b + c

def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    return n


print no_teen_sum(1,2,3)
print no_teen_sum(1,13,1)
print no_teen_sum(2,1,14)
print fix_teen(3)
