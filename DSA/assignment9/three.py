def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N - 1)
print(factorial(5))  # Output: 120
print(factorial(4))  # Output: 24
