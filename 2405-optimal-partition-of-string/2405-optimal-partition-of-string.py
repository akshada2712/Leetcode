class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        res = 0
        
        for i in s:
            if i in chars:
                res += 1
                chars.clear()
                
            chars.add(i)
            
            
        return res+1
        