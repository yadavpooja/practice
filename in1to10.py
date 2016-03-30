def in1to10(n,outside_mode):
    if 1 <= n <=10:
        return True
    elif  n <= 1 or n >= 10 and outside_mode:
        return True
    return False



print in1to10(5,False)
print in1to10(11,False)
print in1to10(11,True)




