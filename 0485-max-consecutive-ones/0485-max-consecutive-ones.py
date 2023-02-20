class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        hashmap = {}
        cnt = 0
        currMax = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            elif nums[i] == 0:
                currMax = max(currMax,cnt)
                cnt = 0
        return max(currMax,cnt)
                
                
                
                
        