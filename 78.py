class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(i, current):
            if i >= len(nums):
                res.append(current[:])
                return
            
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
            backtrack(i + 1, current)
        
        current = []
        backtrack(0, current)
        
        return res
        