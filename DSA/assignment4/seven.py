def max_count(m, n, ops):
    if not ops:
        return m * n
    
    min_row = min(op[0] for op in ops)
    min_col = min(op[1] for op in ops)
    
    return min_row * min_col
m = 3
n = 3
ops = [[2, 2], [3, 3]]
max_integers = max_count(m, n, ops)
print(max_integers)  # Output: 4
