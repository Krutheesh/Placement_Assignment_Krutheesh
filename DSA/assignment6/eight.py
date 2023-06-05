def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            temp = 0
            for idx in range(k):
                temp += mat1[i][idx] * mat2[idx][j]
            result[i][j] = temp

    return result
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(multiply(mat1, mat2))
