def left2(str):
    n = len(str)
    if n < 2:
        return
    else:
        return str[2:] + str[:2]


print left2('hello')
print left2('java')
print left2('hi')

