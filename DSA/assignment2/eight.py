def minScore(nums, k):
    max_val = max(nums)
    min_val = min(nums)

    if max_val - min_val <= 2 * k:
        return 0
    else:
        return max_val - min_val - 2 * k
nums = [1]
k = 0
min_score = minScore(nums, k)
print(min_score)
