class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        abcdcbf
        3,3
        2, 4
        1, 5
        1, 5
        """
        res = (0,0)
    
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1


        for i in range(len(s)):
            odd_length = expand(i, i)
            left, right = res
            if odd_length > right - left + 1:
                dist = odd_length // 2
                res = (i - dist, i + dist)

            left, right = res
            even_length = expand(i, i + 1)
            if even_length > right - left + 1:
                dist = (even_length // 2) - 1
                res = (i - dist, i + 1 + dist)
        

        i, j = res

        return s[i: j+1]
    


                
       

