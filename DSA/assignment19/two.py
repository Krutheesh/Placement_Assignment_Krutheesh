from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n
        sortedList = SortedList()
        for i in range(n - 1, -1, -1):
            index = sortedList.bisect_left(nums[i])
            ans[i] = index
            sortedList.add(nums[i])
        return ans
nums = [5,2,6,1]
a=Solution()
result = a.countSmaller(nums)
print(result)