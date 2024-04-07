class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        runLen = math.inf
        l = 0
        runSum = 0
        
        
        for r in range(len(nums)):
            runSum += nums[r]
            while runSum >= target:
                runLen = min(runLen, r - l + 1)
                runSum -= nums[l]
                l += 1
                
        return runLen if runLen != math.inf else 0
                
                
        