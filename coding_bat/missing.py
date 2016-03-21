def missing(str, x):
    n = len(str) 
    return str[:x] + str[(x+1):n]


print missing('hello',2)
print missing('kitten',0)
print missing('kitten',4)
