class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_ = {}
        
        for i in arr:
            if i not in hash_:
                hash_[i] = 1
            else:
                hash_[i] += 1
                
        unique = set()
        
        for i in hash_.values():
            if i not in unique:
                unique.add(i)
            else:
                return False
            
        return True
        