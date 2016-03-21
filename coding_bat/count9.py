def count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count


print count9([1,2,3,9])
print count9([1,9,3,9])
print count9([1,9,9,9])
