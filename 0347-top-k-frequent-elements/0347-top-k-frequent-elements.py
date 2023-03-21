class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
            
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
        
        
        
        
        
#         hashmap = {}
        
#         for i in nums:
#             if i not in hashmap:
#                 hashmap[i] = 1
#             else:
#                 hashmap[i] += 1
#         res = []       
#         for i in hashmap:
#             if i <= k:
#                 res.append(i)
                
#         return res
                
#         #return all(values >= k for values in hashmap)