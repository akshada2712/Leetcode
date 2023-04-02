class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        n = len(potions)
        potions.sort()
        
        for i in spells:
            l = 0
            r = n - 1 
            while l <=r:
                m = (l+r) // 2
                
                if i * potions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
                    
            res.append(n-l)
            
        return res