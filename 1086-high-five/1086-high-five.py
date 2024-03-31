class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        results =  {}
        
        for id, score in items:
            if id not in results:
                results[id] = []
            results[id].append(score)   
            
        avgScore = []
        
        for i, scores in results.items():
            scores = sorted(scores, reverse = True)
            avgScore.append([i, int(sum(scores[:5]) / 5)])
            
        return sorted(avgScore, key = lambda x:x[0])
        