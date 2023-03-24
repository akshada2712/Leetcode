class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        
        for u,v,w in times:
            edges[u].append((v,w))
            
        minHeap = [(0,k)]
        visit = set()
        t = 0
        
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t = max(t, cost)
            for i, w in edges[node]:
                if i not in visit:
                    heapq.heappush(minHeap, (cost+w,i))
                    
        return t if len(visit) == n else -1
        
        