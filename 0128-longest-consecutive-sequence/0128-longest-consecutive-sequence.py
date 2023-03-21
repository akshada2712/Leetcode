class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        cnt = 1
        maxcnt = 0
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                pass
            elif nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 1
                
            maxcnt = max(maxcnt, cnt)
            
        return maxcnt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nums.sort()
#         maxcount = 0
#         cnt = 1
        
#         for i in range(len(nums)):
#             if nums[i] == nums[i-1]:
#                 pass
#             elif nums[i] == nums[i-1] + 1:
#                 cnt += 1
#             else:
#                 cnt = 1
                
#             maxcount = max(maxcount, cnt)
            
#         return maxcount
            
        