class Solution:
    def distributeCandies(self, C: List[int]) -> int:
        return min(len(set(C)), len(C) // 2)