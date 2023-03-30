class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1,len(nums)):
            dp[i] = dp[i-1] + nums[i]
            
        return dp