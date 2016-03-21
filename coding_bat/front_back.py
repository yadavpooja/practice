def front(str):
    n = len(str)
    if n <= 1:
        return str
    else:
        return str[n-1] + str[1:(n-1)] + str[0]



print front("code")
print front("a")
print front("ab")
print front("abc")
