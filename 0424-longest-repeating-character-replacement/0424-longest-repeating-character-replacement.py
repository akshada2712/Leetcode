class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                
            
            res = max(res, r - l + 1)
            
        return res
        
        
        
        
#         l = 0
#         r = 1
#         hashmap = {}
#         res = 0
        
#         while l <= r and r < len(s):
#             if s[l] in hashmap:
#                 hashmap[s[l]] += 1
#             else:
#                 hashmap[s[l]] = 1
                
#             val = (r - l) - max(hashmap.values())
#             print(val)
#             if val <= k:
#                 r += 1
#                 res = val
#             else:
#                 hashmap[s[l]] -= 1
#                 l += 1
                
                
#             print(res)
            
            
        