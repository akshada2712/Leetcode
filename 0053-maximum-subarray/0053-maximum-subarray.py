class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        currSum = 0
        
        for num in nums:
            currSum += num
            ans = max(ans, currSum)
            
			# if currSum < 0 then why to accumulate it further just ignore it and make it 0
            if currSum < 0:
                currSum = 0
        
        return ans