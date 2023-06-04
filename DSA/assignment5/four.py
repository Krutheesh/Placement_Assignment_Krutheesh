def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)

    return [diff1, diff2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(findDisappearedNumbers(nums1, nums2))
