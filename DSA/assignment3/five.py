def arrange_coins(n):
    left = 0
    right = n
    
    while left <= right:
        k = (left + right) // 2
        curr = k * (k + 1) // 2
        
        if curr == n:
            return k
        
        if curr > n:
            right = k - 1
        else:
            left = k + 1
    
    return right
n = 5
complete_rows = arrange_coins(n)
print(complete_rows) 