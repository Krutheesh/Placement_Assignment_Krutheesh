def reverse_str(s, k):
    chars = list(s)
    n = len(chars)

    for i in range(0, n, 2 * k):
        left = i
        right = min(i + k - 1, n - 1)

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return ''.join(chars)
s = "abcdefg"
k = 2
print(reverse_str(s, k))
