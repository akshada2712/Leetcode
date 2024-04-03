class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # using cycle sort  -> give tle
        
#         i = 0
#         n = len(nums) 
        
#         while i < n:
#             curr = nums[i] - 1
#             if nums[i] != nums[curr]:
#                 nums[i], nums[curr] = nums[curr], nums[i]
#             else:
#                 i += 1 
                
#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1
            
#         return n + 1
        
    # create hashmap of all numbers in nums
        hash_ = set(nums)
        
        # check if 1 is present as it is smallest posiitve integer
        if 1 not in hash_:
            return 1 
        
        # run a loop for maxium element + 2  and check if number is present or not
        for i in range(max(nums) + 2):
            if i not in hash_ and i > 0:
                return i 
        
        # return length of numbers if everything is presemt
        return len(nums)
        
#         minNum = min(nums)
#         maxNum = max(nums)
#         if len(nums) == 1 and nums[0] == 1:
#             return 1
        
#         for i in range(1,len(nums)+1):
#             if i not in nums:
#                 return i 
            
        
            
        
        