class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0 
        j = len(height) - 1
        res = 0 
        while i < j:
            res = max(res, min(height[i], height[j]) * j - i - 1)



        return res  