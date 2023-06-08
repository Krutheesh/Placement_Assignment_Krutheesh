def array_pair_sum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum
nums = [1, 4, 3, 2]
maximized_sum = array_pair_sum(nums)
print(maximized_sum)
