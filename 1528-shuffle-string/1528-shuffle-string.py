class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dp = [0] * len(indices)
        
        for i in range(len(s)):
            dp[indices[i]] = s[i]
            
        return ''.join(dp)