class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        @cache
        def backtrack(remaining):
            if not remaining:
                return True

            for word in wordDict:
                if remaining[0:len(word)] == word:
                    if backtrack(remaining[len(word):]):
                        return True
            
            return False

        return backtrack(s)
