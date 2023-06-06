def is_strobogrammatic(num):
    strobogrammatic_digits = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in strobogrammatic_digits or num[right] not in strobogrammatic_digits:
            return False

        if strobogrammatic_digits[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True
num = "69"
print(is_strobogrammatic(num))
