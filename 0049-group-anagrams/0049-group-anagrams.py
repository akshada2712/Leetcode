from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        
        for i in strs:
            key = "".join(sorted(i))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(i)
            
        return hashmap.values()