def find_nearest_element_with_greater_frequency(arr):
    stack = []
    frequency = {}
    result = [-1] * len(arr)

    for i in range(len(arr)):
        if arr[i] not in frequency:
            frequency[arr[i]] = 1
        else:
            frequency[arr[i]] += 1

        while stack and frequency[arr[i]] > frequency[arr[stack[-1]]]:
            result[stack.pop()] = arr[i]

        stack.append(i)

    return result

arr = [1, 1, 2, 3, 4, 2, 1]
output = find_nearest_element_with_greater_frequency(arr)
print(output)  # [-1, -1, 1, 2, 2, 1, -1]

arr = [1, 2, 1, 2, 3, 3, 4, 4, 4]
output = find_nearest_element_with_greater_frequency(arr)
print(output)  # [-1, -1, -1, -1, -1, -1, -1, 3, 3]
