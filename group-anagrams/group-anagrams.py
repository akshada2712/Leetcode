class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
        
#         for w in strs:
#             count = [0] * 26
#             for c in w:
#                 count[ord(c) - ord('a')] += 1 
                
#             res[tuple(count)].append(w)
             
            
#         return list(res.values())

        new_strs = []
    
        for i in range(len(strs)):
            new_strs.append(''.join(sorted(strs[i])))
            
        hashmap = {}
        
        for i in range(len(new_strs)):
            if new_strs[i] not in hashmap:
                hashmap[new_strs[i]] = []
                
            hashmap[new_strs[i]].append(strs[i])
            
        return list(hashmap.values())
    
    
      