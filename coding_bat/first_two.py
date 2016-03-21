def first_two(str):
    n = len(str)
    if n < 2:
        return str
    else:
        return str[:2]


print first_two('hello')
print first_two('h')
print first_two('abc')
print first_two('hiii')
