def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with swapped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Iterate over the rows and columns of the original matrix
    for i in range(rows):
        for j in range(cols):
            # Swap the elements at corresponding positions
            transposed[j][i] = matrix[i][j]
    
    return transposed
