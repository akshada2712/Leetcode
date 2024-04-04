class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        map = Counter(nums)
        pairs = 0
        
        for i in map:
            if ( i + k ) in map:
                pairs += map[i] * map[i + k]
                
        return pairs
#         l = 0
#         r = 1
#         pairs = 0
        
#         while l < r and r < len(nums):
#             print(l, r)
#             if abs(nums[l] - nums[r]) == k:
#                 print('from if',l,r)
#                 pairs += 1
#                 r += 1
#             else:
#                 #l += 1
#                 r = l + 1
            
#         return pairs
                
        
        