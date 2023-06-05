def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    target = n * n
    rowStart = 0
    rowEnd = n - 1
    colStart = 0
    colEnd = n - 1

    while num <= target:
        for col in range(colStart, colEnd + 1):
            matrix[rowStart][col] = num
            num += 1
        rowStart += 1

        for row in range(rowStart, rowEnd + 1):
            matrix[row][colEnd] = num
            num += 1
        colEnd -= 1

        if rowStart <= rowEnd:
            for col in range(colEnd, colStart - 1, -1):
                matrix[rowEnd][col] = num
                num += 1
            rowEnd -= 1

        if colStart <= colEnd:
            for row in range(rowEnd, rowStart - 1, -1):
                matrix[row][colStart] = num
                num += 1
            colStart += 1

    return matrix


n = 3
print(generateMatrix(n))
