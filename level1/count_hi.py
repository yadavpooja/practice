def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i + 2]  == 'hi':

            count += 1
    return count


print count_hi('abc hi ho')
print count_hi('abchihi')
print count_hi('hihi')

