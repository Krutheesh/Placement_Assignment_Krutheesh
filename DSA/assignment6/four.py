def findMaxLength(nums):
    max_length = 0
    count = 0
    sum_indices = {0: -1}

    for i, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            count -= 1

        if count in sum_indices:
            length = i - sum_indices[count]
            if length > max_length:
                max_length = length
        else:
            sum_indices[count] = i

    return max_length
nums = [0, 1]
print(findMaxLength(nums))
