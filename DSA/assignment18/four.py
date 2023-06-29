def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    # Find the minimum and maximum values in the array
    min_num = min(nums)
    max_num = max(nums)
    
    # Compute the size of each bucket
    bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
    bucket_count = (max_num - min_num) // bucket_size + 1
    
    # Initialize the buckets with empty lists
    buckets = [[] for _ in range(bucket_count)]
    
    # Assign each number to the corresponding bucket
    for num in nums:
        index = (num - min_num) // bucket_size
        buckets[index].append(num)
    
    # Find the maximum gap between buckets
    max_gap = 0
    prev_max = min_num
    for bucket in buckets:
        if not bucket:
            continue
        min_bucket = min(bucket)
        max_bucket = max(bucket)
        max_gap = max(max_gap, min_bucket - prev_max)
        prev_max = max_bucket
    
    return max_gap

# Example usage
nums = [3, 6, 9, 1]
max_diff = maximumGap(nums)
print(max_diff)
