def common_end(a,b):
    n = len(a)
    m = len(b)
    if n < 1 or m < 1:
        return
    elif a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False


print common_end([1,2,3],[7,3])
print common_end([1,2,3],[7,3,2])
print common_end([1,2,3],[1,3])
print common_end([1,2,3],[])
