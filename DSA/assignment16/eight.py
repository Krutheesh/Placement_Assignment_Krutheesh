def max_absolute_difference(arr):
    n = len(arr)
    LS = [0] * n
    RS = [0] * n
    stack = []

    # Find the nearest smaller element on the right (RS)
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            RS[stack.pop()] = arr[i]
        stack.append(i)

    stack = []

    # Find the nearest smaller element on the left (LS)
    for i in range(n - 1, -1, -1):
        while stack and arr[i] < arr[stack[-1]]:
            LS[stack.pop()] = arr[i]
        stack.append(i)

    max_diff = 0

    # Find the maximum absolute difference
    for i in range(n):
        max_diff = max(max_diff, abs(LS[i] - RS[i]))

    return max_diff

# Example usage
arr = [2, 1, 8]
result = max_absolute_difference(arr)
print(result)
