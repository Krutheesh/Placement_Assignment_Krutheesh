def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first pair where nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        j = n - 1
        # Find the smallest element in the subarray nums[i+1:] that is greater than nums[i]
        while j > i and nums[j] <= nums[i]:
            j -= 1
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray nums[i+1:]
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
nums = [1, 2, 3]
next_permutation = nextPermutation(nums)
print(next_permutation)
