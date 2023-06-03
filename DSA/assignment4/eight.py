def shuffle_array(nums, n):
    shuffled = []
    for i in range(n):
        shuffled.append(nums[i])
        shuffled.append(nums[i+n])
    return shuffled
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle_array(nums, n)
print(result)  # Output: [2, 3, 5, 4, 1, 7]
