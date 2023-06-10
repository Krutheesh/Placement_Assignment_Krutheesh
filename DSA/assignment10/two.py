def lastRemaining(n):
    if n == 1:
        return 1
    return 2 * (n // 2 + 1 - lastRemaining(n // 2))

print(lastRemaining(9))  # Output: 6
print(lastRemaining(1)) #output : 1