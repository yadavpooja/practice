def extra_end(str):
    n = len(str)
    if n < 2:
        return 
    else:
        return str[-2:] * 3


print extra_end('hello')
print extra_end('h')
print extra_end('ab')
print extra_end('flower')

