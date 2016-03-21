def first_last6(nums):
    n = len(nums)
    if n < 1:
        return
    elif nums[n-1] == 6 or nums[0] == 6:
        return True
    else:
        return False



print first_last6([1,2,6])
print first_last6([6,1,2,3])
print first_last6([1,2,3,4])
