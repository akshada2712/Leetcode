class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        
        
        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                
        res = []
        
        for i in hashmap:
            if hashmap[i] == i:
                res.append(i)
         
        return max(res) if len(res) >= 1 else -1
        