def non_start(a,b):
    n = len(a)
    m = len(b)
    if n < 1 or m < 1:
        return
    else:
        return a[1:] + b[1:]



print non_start('hello','there')
print non_start('java','code')
print non_start('shotl','java')
