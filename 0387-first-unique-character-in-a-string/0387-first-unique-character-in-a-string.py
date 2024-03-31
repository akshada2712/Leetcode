class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnts = Counter(s)
        
        for i in range(len(s)):
            if cnts[s[i]] == 1:
                return i 
            
        return -1
        