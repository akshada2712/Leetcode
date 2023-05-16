class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hashmap = set()
        
        for i in range(1,len(nums)):
            currSum = nums[i] + nums[i-1]
            if currSum in hashmap:
                return True
            hashmap.add(currSum)
            
        return False
        