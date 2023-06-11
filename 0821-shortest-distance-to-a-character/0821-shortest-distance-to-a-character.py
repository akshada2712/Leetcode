class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dist = set()
        
        dp = [None] * len(s)
        for i in range(len(s)):
            if s[i] == c:
                dist.add(i)
                
        for i in range(len(s)):
            minDist = float('inf')
            for j in dist:
                minDist = min(minDist,abs(i - j))
                
            dp[i] = minDist 
            
        return dp
                
        