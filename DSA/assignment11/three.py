def missingNumber(nums):
    n = len(nums)
    missing = n

    for i in range(n):
        missing ^= i ^ nums[i]

    return missing
print(missingNumber([3, 0, 1]))  # Output: 2
print(missingNumber([0, 1]))  # Output: 2
