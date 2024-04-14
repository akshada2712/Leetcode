class Solution:
    def scoreOfString(self, s: str) -> int:
        
        arr = [0] * (len(s) )
        
        for i in  range(len(s)):
            arr[i] = ord(s[i])
        
        diff = 0
        for i in range(1, len(s)):
            diff += abs(arr[i-1] - arr[i])
            
        return diff
            
         