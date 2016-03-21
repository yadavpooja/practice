def string(str):
    result = ''
    n = len(str)
    for i in range(n):
        result = result + str[:i + 1]
    return result


print string('code')
print string('abc')
print string('ab')
