def rotate_left3(nums):
    a = nums[0]
    nums.remove(a)
    nums.append(a)
    return nums


print rotate_left3([1,2,3])
print rotate_left3([11,9,5])
print rotate_left3([0,0,7])
