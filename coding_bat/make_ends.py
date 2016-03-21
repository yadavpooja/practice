def make_ends(nums):
    n = len(nums)
    if n < 1:
        return
    else:
        return [nums[0],nums[-1]]



print make_ends([1,2,3])
print make_ends([1,2,3,4])
print make_ends([1,2,343,4,5])
