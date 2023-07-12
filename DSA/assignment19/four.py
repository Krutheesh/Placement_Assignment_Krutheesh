def moveZeroes(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] != 0:
            left += 1
        elif nums[right] == 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

nums = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
moveZeroes(nums)
print(nums)  

nums = [1, 2, 0, 4, 3, 0, 5, 0]
moveZeroes(nums)
print(nums)  

nums = [1, 2, 0, 0, 0, 3, 6]
moveZeroes(nums)
print(nums)  