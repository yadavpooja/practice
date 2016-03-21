def without_end(str):
    n = len(str)
    if n < 2:
        return
    else:
        return str[1:n-1]


print without_end('hello')
print without_end('java')
print without_end('coding')
