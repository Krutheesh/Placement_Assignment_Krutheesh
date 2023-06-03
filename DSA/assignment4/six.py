def sorted_squares(nums):
    squared_nums = [num ** 2 for num in nums]
    squared_nums.sort()
    return squared_nums
nums = [-4, -1, 0, 3, 10]
squared_sorted = sorted_squares(nums)
print(squared_sorted)  # Output: [0, 1, 9, 16, 100]
