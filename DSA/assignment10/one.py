def is_power_of_three(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return is_power_of_three(n // 3)
print(is_power_of_three(27))  # Output: True
print(is_power_of_three(0))   # Output: False
