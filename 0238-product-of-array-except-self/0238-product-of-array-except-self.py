import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        # calculating prefixes

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
            
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
            
        return res
        
        
        
        
        
#         nums_set = set(nums)
        
#         def prod(nums):
#             print(nums)
#             res = 1
#             for i in nums:
#                 res = res * i
#                 #print(res,i)
#             return res
#         prod_arr = [0] * len(nums)
#         for i in range(len(nums)):
#             nums_set.remove(nums[i])
#             prod_arr[i] = prod(nums_set)
#             nums_set.add(nums[i])
            
            
#         return prod_arr
        