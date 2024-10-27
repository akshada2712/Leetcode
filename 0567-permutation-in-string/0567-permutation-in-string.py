class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        
        if l1 > l2:
            return False 
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:l1])
        
        if s1_count == window_count:
            return True 
        
        for i in range(l1, l2):
            window_count[s2[i]] += 1 
            
            window_count[s2[i-l1]] -= 1
            
            if window_count[s2[i-l1]] == 0:
                del window_count[s2[i-l1]]
                
            if s1_count == window_count:
                return True 
            
        return False 
#         count_s1 = Counter(s1)
        
#         window_size = len(s1)
        
#         l = 0
#         r = window_size + l
        
#         while r <= len(s2):
#             #print(l,r)
#             if Counter(s2[l:r]) == count_s1:
#                 return True 
            
#             l += 1
#             r += 1
            
#         return False
            
        