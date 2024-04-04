class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        m = len(multipliers)
        n = len(nums)
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)] # extra row and columns
        #print(dp)
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                right = ( n - 1) - ( i - left)
                mul = multipliers[i]
                
                dp[i][left] = max(
                                  mul * nums[left] + dp[i + 1][left + 1],
                                  mul * nums[right] + dp[i + 1][left])
                
        return dp[0][0]
        