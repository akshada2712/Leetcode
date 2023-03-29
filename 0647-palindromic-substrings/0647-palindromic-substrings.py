class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPali(s,l,r):
            resLen = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                resLen += 1
                l -= 1
                r += 1
            return resLen
        res = 0
        for i in range(len(s)):
            res += isPali(s,i,i)
            res += isPali(s,i,i+1)
            
        return res
            
            