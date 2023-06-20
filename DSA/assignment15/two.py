def find_nearest_smaller_elements(arr):
    stack = []  # To store the elements
    result = [-1] * len(arr)  # Initialize result array with -1
    
    for i in range(len(arr)):
        while stack and arr[i] <= stack[-1]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result
arr = [1, 6, 2]
output = find_nearest_smaller_elements(arr)
print(output)
