class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def dfs(i, curr, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            if remaining < 0 or i >= len(candidates):
                return
            
            # decision to use candidate
            curr.append(candidates[i])
            dfs(i, curr, remaining - candidates[i])

            # decision to not use candidate
            curr.pop()
            dfs(i+1, curr, remaining)
        
        dfs(0, [], target)
        return res
