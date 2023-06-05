def moveZeroes(nums):
    n = len(nums)
    left = 0  
    right = 0  

    while right < n:
        if nums[right] != 0:
           
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
# Example 1
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Example 2
nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]
