class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        k = len(s1)
        
        for i,val in enumerate(s2):
            c2[val] += 1
            
            if i >= k:
                
                c2[s2[i-k]] -= 1
                
            if c1 == c2:
                return True
            
        return False
                
            