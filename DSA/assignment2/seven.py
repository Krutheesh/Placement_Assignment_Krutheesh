def isMonotonic(nums):
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            is_increasing = False
        if nums[i] > nums[i - 1]:
            is_decreasing = False
            
    return is_increasing or is_decreasing
nums = [1, 2, 2, 3]
is_monotonic = isMonotonic(nums)
print(is_monotonic)
