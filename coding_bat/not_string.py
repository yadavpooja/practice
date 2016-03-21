def string(str):
    if str[:3] == 'not':
        return str
    else:
        return 'not' + str


print string('candy')
print string('x')
print string('notbad')
