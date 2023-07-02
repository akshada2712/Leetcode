class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        l = 0
        curr = 0
        res = 0
        ctr = Counter()
        for r in range(len(nums)):
            ctr[nums[r]] += 1
            curr += nums[r]
            
            while ctr[nums[r]] > 1 or (r - l + 1) > k:
                curr -= nums[l]
                ctr[nums[l]] -= 1
                l += 1
                
            if (r - l + 1) == k:
                res = max(res, curr)
                
        return res
            
            
        
        
        # currSum = 0
        # maxSum = 0
        # seen = set()
        
#         for i in range(len(nums)):
#             if nums[i] not in seen:
#                 if len(seen) < k:
#                     seen.add(nums[i])
#                     currSum += nums[i]
                
#                 if len(seen) == k:
#                     maxSum = max(maxSum, currSum)
#                     currSum -= nums[i - k + 1]
#                     seen.remove(nums[i- k + 1])
#             else:
#                 seen = {nums[i]}
#                 currSum = nums[i]
#         return maxSum
    
        