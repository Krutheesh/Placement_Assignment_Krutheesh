def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Find the intersection point of the two pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Move one pointer to the beginning of the array
    slow = nums[0]

    # Move both pointers at the same speed until they meet again
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3,1,3,4,2]))# output : 3