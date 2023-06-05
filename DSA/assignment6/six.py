def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    freqMap = {}
    for num in changed:
        freqMap[num] = freqMap.get(num, 0) + 1

    original = []
    for num in sorted(changed):
        if freqMap.get(num, 0) == 0:
            continue

        if freqMap.get(num * 2, 0) == 0:
            return []

        original.append(num)
        freqMap[num] -= 1
        freqMap[num * 2] -= 1

    return original
changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))
