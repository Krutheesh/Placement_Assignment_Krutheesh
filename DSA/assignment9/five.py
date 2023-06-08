def findMax(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n - 1], findMax(arr, n - 1))
arr1 = [1, 4, 3, -5, -4, 8, 6]
print(findMax(arr1, len(arr1)))  # Output: 8

arr2 = [1, 4, 45, 6, 10, -8]
print(findMax(arr2, len(arr2)))  # Output: 45
