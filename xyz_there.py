def xyz_there(str):
    flag = False
    for i in range(len(str)-2):
        sub = str[i:i+3]
        if sub == 'xyz':
            if str[i-1] == '.':
                continue
            else:
                flag = True
    return flag


print xyz_there('abcxyz')
print xyz_there('abc.xyz')
print xyz_there('xyz.abc')
