class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        i,j,ans = 0,k,k
        
        while j <= len(blocks):
            cnt = blocks[i:j].count('W')
            ans = min(ans, cnt)
            i += 1
            j += 1
        
        return ans
        
#         minC = float("inf")
#         if len(blocks) == k:
#             return Counter(blocks)['W']
        
#         for i in range(len(blocks)):
#             if i + k > len(blocks):
#                 print('iiii')
#                 return minC
#             hash_ = Counter(blocks[i:k])
            
#             minC = min(minC, hash_['W'])
            