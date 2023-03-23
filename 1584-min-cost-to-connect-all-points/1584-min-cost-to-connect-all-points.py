class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        adj ={i:[] for i in range(n)}   #i : list of [cost,node]
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
                
                
        # prims' algo
        res = 0
        visit = set()
        minHeap = [[0,0]]        #[cost,point]
        while len(visit) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for iCost, i in adj[node]:
                if i not in visit:
                    heapq.heappush(minHeap,[iCost, i])
                    
        return res
                
            
            
        