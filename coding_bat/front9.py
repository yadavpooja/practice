def front9(nums):
    n = len(nums)
    for i in nums[:4]:
        if i == 9:
            return True
    return False



print front9([1,2,3,9,7])
print front9([1,2,3,4,7])
print front9([1,2,3,0,7])

