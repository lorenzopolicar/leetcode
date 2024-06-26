class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res = [] 
        if not digits:
            return res
    

        def dfs(i, current):
            if i == len(digits):
                res.append(current)
                return
            
            for letter in mapping[digits[i]]:
                dfs(i + 1, current + letter)
        
        dfs(0, "")

        return res

            
            

        