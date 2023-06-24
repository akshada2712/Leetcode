class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ts = sum(nums)
        ls = 0
        
        for i in range(len(nums)):
            rs = ts - nums[i] - ls
            if rs == ls:
                return i
            ls += nums[i]
            
        return -1
            