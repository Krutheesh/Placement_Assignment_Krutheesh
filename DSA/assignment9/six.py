def findNthTermRecursive(a, d, N):
    if N == 1:
        return a
    else:
        return findNthTermRecursive(a + d, d, N - 1)
print(findNthTermRecursive(2, 1, 5))  # Output: 6
print(findNthTermRecursive(5, 2, 10))  # Output: 23
