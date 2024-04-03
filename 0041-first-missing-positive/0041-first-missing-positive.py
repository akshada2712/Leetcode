class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hash_ = set(nums)
        
        if 1 not in hash_:
            return 1 
        
        for i in range(max(nums) + 2):
            if i not in hash_ and i > 0:
                return i 
            
        return len(nums)
        
#         minNum = min(nums)
#         maxNum = max(nums)
#         if len(nums) == 1 and nums[0] == 1:
#             return 1
        
#         for i in range(1,len(nums)+1):
#             if i not in nums:
#                 return i 
            
        
            
        
        