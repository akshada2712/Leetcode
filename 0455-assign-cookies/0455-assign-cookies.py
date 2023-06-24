class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i = 0
        cnt = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt+= 1
                j += 1
                i += 1
            else:
                j += 1
                
                
        return cnt