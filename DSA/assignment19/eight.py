def intersect(nums1, nums2):
    count1 = {}
    count2 = {}

    for num in nums1:
        count1[num] = count1.get(num, 0) + 1

    for num in nums2:
        count2[num] = count2.get(num, 0) + 1

    intersection = []

    for num in count1:
        if num in count2:
            freq = min(count1[num], count2[num])
            intersection.extend([num] * freq)

    return intersection

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)  # Output: [2, 2]
