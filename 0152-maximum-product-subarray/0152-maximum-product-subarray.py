class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1,1
        res = max(nums)
        for i in nums:
            if i == 0:
                currMin, currMax = 1,1
                
            tmp = i * currMax
            currMax = max(tmp,i,i*currMin)
            currMin = min(tmp,i,i*currMin)
            res = max(res,currMax)
            
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = max(nums)
#         curMax, curMin = 1,1
        
#         for i in nums:
#             if i == 0:
#                 curMax, curMin = 1,1
#                 continue
#             tmp = i * curMax
#             curMax = max(tmp, i * curMin, i)
#             curMin = min(tmp, i * curMin, i)
#             res = max(res, curMax)
            
#         return res
                