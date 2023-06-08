def search(nums, target):
    return binarySearch(nums, target, 0, len(nums) - 1)

def binarySearch(nums, target, start, end):
    if start > end:
        return -1

    middle = (start + end) // 2
    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        return binarySearch(nums, target, middle + 1, end)
    else:
        return binarySearch(nums, target, start, middle - 1)
nums = [-1, 0, 3, 5, 9, 12]
target = 9
index = search(nums, target)
print(index)
