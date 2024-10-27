class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        
        window_size = len(s1)
        
        l = 0
        r = window_size + l
        
        while r <= len(s2):
            print(l,r)
            if Counter(s2[l:r]) == count_s1:
                return True 
            
            l += 1
            r += 1
            
        return False
            
        