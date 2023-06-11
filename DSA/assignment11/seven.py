def searchRange(nums, target):
    left = findLeftMost(nums, target)
    right = findRightMost(nums, target)
    return [left, right]


def findLeftMost(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid - 1
            if nums[mid] == target:
                result = mid
        else:
            left = mid + 1

    return result


def findRightMost(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
            if nums[mid] == target:
                result = mid
        else:
            right = mid - 1

    return result
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1, -1]
