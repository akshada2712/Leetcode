class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for tar in range(1,n+1):
            for s in range(1,tar+1):
                sq = s * s
                if tar - sq < 0:
                    break
                dp[tar] = min(dp[tar], 1 + dp[tar - sq])
                
        # print(dp)
        
        return dp[n]
        