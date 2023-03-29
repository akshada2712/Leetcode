class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        
        _sum, score = 0,0
        
        for s in satisfaction:
            _sum += s
            
            if _sum < 0: 
                break
            score += _sum
            
        return score
        