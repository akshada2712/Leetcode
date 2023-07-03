class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        bask = {}
        cnt = 0
        l = 0
        for r in range(len(fruits)):
            if fruits[r] not in bask:
                bask[fruits[r]] = 1
            else:
                bask[fruits[r]] += 1
            
            while len(bask) > 2:
                bask[fruits[l]] -= 1
                if bask[fruits[l]] == 0:
                    del bask[fruits[l]]
                l += 1
                
            cnt = max(cnt, r - l + 1)
        return cnt
                
        