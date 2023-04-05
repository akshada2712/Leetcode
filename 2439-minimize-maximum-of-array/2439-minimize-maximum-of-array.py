class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        currSum = 0
        
        for i in range(len(nums)):
            currSum += nums[i]
            
            res = max(res, ceil(currSum / (i + 1)))
            
        return res
            
        