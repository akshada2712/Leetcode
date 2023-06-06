class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        
        for i in range(len(edges)):
            src, dst = edges[i]
            graph[src].append([dst, succProb[i]])
            graph[dst].append([src, succProb[i]])
            
        pq = [(-1, start)]    
        visit = set()
        while pq:
            prob, node = heapq.heappop(pq)
            visit.add(node)
            if node == end:
                return prob * -1
            for nei, probi in graph[node]:
                if nei not in visit:
                    heapq.heappush(pq, (probi * prob, nei))
                    
        return 0.0
            
        
        