class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        runSum = 0
        runLen = math.inf
        for r in range(len(nums)):
            runSum += nums[r]
            
            while runSum >= target:
                runLen = min(runLen, r - l + 1)
                runSum -= nums[l]
                l += 1
                
        return runLen if runLen != math.inf else 0
        