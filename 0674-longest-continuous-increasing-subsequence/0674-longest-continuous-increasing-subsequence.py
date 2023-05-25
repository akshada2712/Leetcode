class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        tmp = 1
        cnt = 1
        
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                tmp += 1
                cnt = max(tmp,cnt)
            else:
                tmp = 1
                
        return cnt