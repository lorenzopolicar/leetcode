class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        @cache
        def dp(i, total):
            nonlocal res
            if i >= len(nums):
                res = max(res, total)
                return
            dp(i + 1, total)
            dp(i + 2, total + nums[i])
        dp(0, 0)
        return res


