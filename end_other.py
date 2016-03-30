def end_other(a,b):
    x = len(a)
    y = len(b)
    if x < y:
        if b[-x:] == a:
            return True
    if y < x:
        if a[-y:] == b:
            return True
    return False
   # if  x < y and b[-x:] == a:
    #    return True
    #elif y < x and a[-y:] == b:
     #   return True
    #return False


print end_other('hiabc','abc')
print end_other('abc','hiabc')
print end_other('hxadiabc','abc')



