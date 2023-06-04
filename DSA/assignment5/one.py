def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []

    result = [[0] * n for _ in range(m)]
    for i in range(len(original)):
        row = i // n
        col = i % n
        result[row][col] = original[i]

    return result

original = [1, 2, 3, 4]
m = 2
n = 2
print(convert_to_2d_array(original, m, n))
