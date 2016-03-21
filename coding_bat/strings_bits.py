def string(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result



print string('hello')
print string('hi')
print string('heeololeo')
