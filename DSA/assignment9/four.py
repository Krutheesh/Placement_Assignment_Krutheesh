def powerRecursive(N, P):
    if P == 0:
        return 1
    else:
        return N * powerRecursive(N, P - 1)
print(powerRecursive(5, 2))  # Output: 25
print(powerRecursive(2, 5))  # Output: 32
