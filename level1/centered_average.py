def centered_avg(nums):
    sum = 0
    for i in nums:
        sum += i
    return (sum - min(nums) - max(nums)) / (len(nums)-2)




print centered_avg([1,2,3,4,100])
print centered_avg([1,1,5,5,10,8,7])
print centered_avg([-10,-4,-2,-4,-2,0])

