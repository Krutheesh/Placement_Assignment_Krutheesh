from collections import Counter

def findLHS(nums):
    num_counts = Counter(nums)
    max_length = 0
    
    for num in num_counts:
        if num + 1 in num_counts:
            length = num_counts[num] + num_counts[num + 1]
            max_length = max(max_length, length)
    
    return max_length
nums = [1, 3, 2, 2, 5, 2, 3, 7]
longest_harmonious_subsequence_length = findLHS(nums)
print(longest_harmonious_subsequence_length)
