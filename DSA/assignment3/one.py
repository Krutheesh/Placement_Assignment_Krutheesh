def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                return curr_sum

            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum

            if curr_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum
nums = [-1, 2, 1, -4]
target = 1
closest_sum = threeSumClosest(nums, target)
print(closest_sum)
