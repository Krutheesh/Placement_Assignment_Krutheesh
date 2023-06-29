def isBadVersion(version):
    return version >= bad

def firstBadVersion(n):
    left = 1
    right = n
    
    while left < right:
        mid = left + (right - left) // 2
        
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage
n = 5
bad = 4
first_bad = firstBadVersion(n)
print(first_bad)
