def containsDuplicate(nums):
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False

# Example usage
nums = [1, 2, 3, 1]
has_duplicates = containsDuplicate(nums)
print(has_duplicates)
