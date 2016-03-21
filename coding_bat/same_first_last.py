def same_first_last(nums):
    n = len(nums)
    if n < 1:
        return
    elif nums[0] == nums[n-1]:
        return True
    else:
        return False


print same_first_last([1,23,3,1])
print same_first_last([1,23,4])
print same_first_last([])
