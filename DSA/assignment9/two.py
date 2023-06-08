def sumOfNaturalNumbers(n):
    if n == 1:
        return 1
    else:
        return n + sumOfNaturalNumbers(n - 1)
print(sumOfNaturalNumbers(3))  # Output: 6
print(sumOfNaturalNumbers(5))  # Output: 15
