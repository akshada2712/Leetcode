class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
                
            hashmap.add(s[r])
            res = max(res, r-l+1)
            
        return res
#         cnt = 0
#         maxcnt = 0
#         for i in s:
#             if i not in hashmap:
#                 hashmap.add(i)
#                 cnt += 1
#             else:
#                 cnt = 0
#                 hashmap.clear()
#                 s = s[i+1:]
                
#             maxcnt = max(cnt, maxcnt)
                
#         return maxcnt
                
        