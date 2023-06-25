class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        cnt = 0
        
        for i in range(len(exp)):
            if exp[i] != heights[i]:
                cnt += 1
                
        return cnt
        