
def front(str,x):
    n = len(str)
    if n < 3:
        return str * x
    else:
        return str[:3] * x


print front('chocolate',2)
print front('chocolate',4)
print front('ce',2)
