def sum2(nums):
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]



print sum2([1,2,3])
print sum2([1,1,1])
print sum2([1])
