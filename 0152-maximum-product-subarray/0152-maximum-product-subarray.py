class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1
        
        for i in nums:
            if i == 0:
                curMax, curMin = 1,1
                continue
            tmp = i * curMax
            curMax = max(tmp, i * curMin, i)
            curMin = min(tmp, i * curMin, i)
            res = max(res, curMax)
            
        return res
                