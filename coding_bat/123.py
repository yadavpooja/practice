def array(nums):
    n = len(nums)
    for i in range(n-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


print array([1,2,3,4,4])
print array([1,2,5,67,7])
print array([1,1,1,2,2,3])
