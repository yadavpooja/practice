def combo_str(a,b):
    n = len(a)
    m = len(b)
    if n == m:
        return
    elif n < m:
        return a + b + a
    elif m < n:
        return b + a + b

print combo_str('hello','hii')
print combo_str('hey','riya')
print combo_str('hii','hii')

