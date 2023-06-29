def find132pattern(nums):
    stack = []
    third = float('-inf')
    
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])
    
    return False
nums = [1, 2, 3, 4]
print(find132pattern(nums))
