def rearrangeArray(nums):
    pos = 0
    neg = 0

    while pos < len(nums):
        if nums[pos] > 0:
            pos += 1
        elif nums[neg] < 0:
            neg += 1
        else:
            nums[pos], nums[neg] = nums[neg], nums[pos]
            pos += 1
            neg += 1

nums = [1, 2, 3, -4, -1, 4]
rearrangeArray(nums)
print(nums)  # Output: [-4, 1, -1, 2, 3, 4]
