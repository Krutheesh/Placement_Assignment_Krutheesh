def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    max_num = max(changed)
    count = [0] * (max_num + 1)
    for num in changed:
        count[num] += 1

    original = []
    for num in range(max_num + 1):
        while count[num] > 0:
            if num % 2 == 0 and count[num // 2] > 0:
                original.append(num // 2)
                count[num] -= 1
                count[num // 2] -= 1
            else:
                return []

    return original
changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))
