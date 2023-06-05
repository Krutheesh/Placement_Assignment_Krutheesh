def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    low = 0
    high = m * n - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

print(searchMatrix(matrix, target))
