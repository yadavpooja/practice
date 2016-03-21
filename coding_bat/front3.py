def front3(str):
    n = len(str)
    if n < 3:
        return str + str + str
    else:
        return str[:3] + str[:3] +str[:3]


print front3('java')
print front3('chocolate')
print front3('abc')
print front3('hi')
