def findMissingRanges(nums, lower, upper):
    result = []
    prev = lower - 1

    for num in nums + [upper + 1]:
        if num - prev > 1:
            result.append(formatRange(prev + 1, num - 1))
        prev = num

    return result

def formatRange(start, end):
    if start == end:
        return [start]
    else:
        return [start, end]
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)
