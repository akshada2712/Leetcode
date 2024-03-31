import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        results =  defaultdict(list)
        # Using maxHeap 
        
        for id, scores in items:
           
                
            heapq.heappush(results[id], scores)
           
        avgScore = []
        for i, score in results.items():
            scores = heapq.nlargest(5, score)
            avgScore.append([i, int(sum(scores) / 5)])
            
        return sorted(avgScore, key = lambda x:x[0])
            
                
        
#         for id, score in items:
#             if id not in results:
#                 results[id] = []
#             results[id].append(score)   
            
#         avgScore = []
        
#         for i, scores in results.items():
#             scores = sorted(scores, reverse = True)
#             avgScore.append([i, int(sum(scores[:5]) / 5)])
            
#         return sorted(avgScore, key = lambda x:x[0])


        
    
        
        