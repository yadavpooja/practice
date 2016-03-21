def max(nums):

    if nums[0] > nums[-1]:
        nums[1] = nums[0]
        nums[2] = nums[0]
        return nums
    else:
        nums[1] = nums[2]
        nums[0] = nums[2]
        return nums


print max([1,2,3])
print max([11,5,9])
print max([7,0,4])
