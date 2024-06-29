class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        res = ""
        i = 0
        sign = 1

        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1 
    
        while i < len(s) and s[i].isnumeric():
            res += s[i]
            i += 1 
        
        if not res:
            return 0
            
        res = int(res) * sign
        res = min(max(res,  -2**31),  2**31 - 1)
        return res
    


