class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        letters = Counter(p)
        res = [] 
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:i+len(p)]) == letters:
                res.append(i)
        return res