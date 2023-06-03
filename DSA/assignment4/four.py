def array_pair_sum(nums):
    nums.sort()
    n = len(nums)
    pair_sum = 0
    
    # Pair the smallest elements together
    for i in range(0, n, 2):
        pair_sum += nums[i]
    
    return pair_sum