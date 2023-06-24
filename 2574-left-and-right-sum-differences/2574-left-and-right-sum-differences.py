class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre = 0
        suf = sum(nums)
        ans = []
        for i in nums:
            pre += i
            ans.append(abs(pre-suf))
            suf -= i
            
        return ans
        
#         ls = [0] * len(nums)
#         rs = [0] * len(nums)
#         res = [0] * len(nums)
        
#         for i in range(1,len(nums)):
#             ls[i] = sum(nums[0:i])
        
#         for i in range(len(nums)-2, -1,-1):
#             rs[i] = sum(nums[i+1:])
            
#         for i in range(len(ls)):
#             res[i] = abs(ls[i] - rs[i])
            
#         return res
        
        