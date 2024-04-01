class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # modified two sum 
        
        map = collections.defaultdict(int)
        
        pairs = 0
        
        for t in time:
            if t % 60 == 0:
                pairs += map[t%60]
            else:
                pairs += map[60 - t%60]
                
            map[t%60] += 1 
            
        return pairs