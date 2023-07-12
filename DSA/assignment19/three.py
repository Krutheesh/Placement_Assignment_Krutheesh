def sortArray(nums):
    def mergeSort(nums, start, end):
        if start >= end:
            return [nums[start]]

        mid = (start + end) // 2
        left = mergeSort(nums, start, mid)
        right = mergeSort(nums, mid + 1, end)

        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    return mergeSort(nums, 0, len(nums) - 1)

nums = [5, 2, 3, 1]
result = sortArray(nums)
print(result)  # Output: [1, 2, 3, 5]
