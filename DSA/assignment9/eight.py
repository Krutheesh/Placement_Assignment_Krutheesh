def productOfArray(arr, n):
    if n == 0:
        return 1
    else:
        return arr[n - 1] * productOfArray(arr, n - 1)
arr1 = [1, 2, 3, 4, 5]
print(productOfArray(arr1, len(arr1)))  # Output: 120

arr2 = [1, 6, 3]
print(productOfArray(arr2, len(arr2)))  # Output: 18
