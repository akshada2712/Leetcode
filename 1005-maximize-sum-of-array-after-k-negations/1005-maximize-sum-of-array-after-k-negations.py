class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
#         while k > 0:
#             nums.sort()
#             nums[0] = -nums[0]
#             k -= 1
            
#         return sum(nums)
    
        # 2nd approach
        
        heapq.heapify(nums)
        
        for _ in range(k):
            heapq.heappush(nums, -heapq.heappop(nums))
        
        return sum(nums)