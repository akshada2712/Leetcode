import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float(inf)] * n
        pq = []
        
        heappush(pq,(0,0,src))
        visit = set()
       
        
        graph = defaultdict(list)
        
        for a,b,c in flights:
            graph[a].append((b,c))
            
        while pq:
            currCost, hops, node = heappop(pq)
            if node == dst:
                return currCost
            
            if (node,currCost) in visit or hops > k:
                continue
                            
            visit.add((node, currCost))
            for nei,cost in graph[node]:
                heappush(pq,(currCost + cost,hops+1,nei))
                
            
        return -1
                
                
        
        
        