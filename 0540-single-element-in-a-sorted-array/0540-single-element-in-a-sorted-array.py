class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # binary search soln
        
        l = 0
        r = len(nums)
        
        while l <= r:
            m = (l+r) // 2
            
            if ((m - 1 < 0 or nums[m-1] != nums[m]) and
                (m + 1 == len(nums) or nums[m + 1] != nums[m])):
                    return nums[m]
                
            leftSize = m - 1 if nums[m - 1] == nums[m] else m
            
            if leftSize % 2 == 1:
                r = m - 1
            else:
                l = m + 1
        
        
#         hash_ = Counter(nums)
        
#         for i in hash_:
#             if hash_[i] == 1:
#                 return i