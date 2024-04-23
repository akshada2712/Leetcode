class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0 
        r = 0 
        n = len(s1)
        counter = {}
        hashmap = Counter(s1)
        
        while r < len(s2):
            #print(l,r, counter, hashmap)
            while r - l + 1 <= n:
                #print(s2[r])
                if s2[r] not in counter:
                    #print(s2[r], counter)
                    counter[s2[r]] = 1
                else:
                    counter[s2[r]] += 1
                r += 1
                
            if counter == hashmap:
                return True
            else:
                counter[s2[l]] -= 1
                if counter[s2[l]] == 0:
                    del counter[s2[l]]
                    
                l += 1
                
        return False
                
                
                
            
            
        