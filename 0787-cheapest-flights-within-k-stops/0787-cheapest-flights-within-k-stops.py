class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u,v,p in flights:
            graph[u].append((v,p))
            
        prices = [(0, src, 0)]
        heapq.heapify(prices)
        visit = set()
        while prices:
            cost, node, stops = heapq.heappop(prices)
            
            if node == dst:
                return cost 
            
            if (node, cost) in visit or stops > k:
                continue 
            
            visit.add((node, cost))
            
            for newNode, newCost in graph[node]:
                heapq.heappush(prices, (newCost+cost, newNode, stops + 1))
                
        #print(cost)
        
        return -1
        
        
                
            
            
        