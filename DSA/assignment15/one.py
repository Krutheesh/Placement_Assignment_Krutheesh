def find_next_greater_elements(arr):
    stack = []  # To store the indices of elements
    result = [-1] * len(arr)  # Initialize result array with -1
    
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    
    return result

arr = [1, 3, 2, 4]
output = find_next_greater_elements(arr)
print(output)
