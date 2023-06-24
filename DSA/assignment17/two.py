def max_subarray_sum_circular(nums):
    # Case 1: Maximum subarray sum without wrapping
    max_sum_no_wrap = kadane(nums)

    # Case 2: Maximum subarray sum with wrapping
    # Invert the sign of each element and find the minimum subarray sum
    # Subtract the minimum subarray sum from the total sum to get the maximum sum with wrapping
    total_sum = sum(nums)
    inverted_nums = [-x for x in nums]
    max_sum_with_wrap = total_sum + kadane(inverted_nums)

    # Return the maximum of the two cases
    return max(max_sum_no_wrap, max_sum_with_wrap)


def kadane(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
nums = [1, -2, 3, -2]
result = max_subarray_sum_circular(nums)
print(result)  # Output: 3
