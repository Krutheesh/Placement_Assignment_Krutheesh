class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        result = 0
        numsLen = len(nums)
        for i in range(0, numsLen - 1, 2):
            result += nums[i]
        return result