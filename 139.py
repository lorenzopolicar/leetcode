from functools import cache


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        target = total // 2

        if (total % 2): return False
        
        @cache
        def backtrack(i, current_sum):
            if i >= len(nums) or current_sum > target:
                return False
            if current_sum == target:
                return True
            
            return backtrack(i+1, current_sum + nums[i]) or backtrack(i+1, current_sum)
        
        return backtrack(0, 0)