class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1
        runDiff = float('inf')
        while r < len(nums):
            runDiff = min(runDiff, nums[r]-nums[l])
            l,r = l+1, r + 1
            
        return runDiff
        