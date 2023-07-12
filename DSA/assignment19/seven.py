def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    intersection = set()

    for num in set1:
        if num in set2:
            intersection.add(num)

    return list(intersection)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection(nums1, nums2)
print(result)  # Output: [2]
