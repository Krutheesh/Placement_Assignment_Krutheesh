def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return sorted(result)
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
