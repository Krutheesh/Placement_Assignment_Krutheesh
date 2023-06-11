def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)
print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(intersection([4,9,5], [9,4,9,8,4])) # output: [9,4]