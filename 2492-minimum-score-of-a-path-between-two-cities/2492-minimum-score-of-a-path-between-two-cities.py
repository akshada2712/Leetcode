class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)   # node -> list of (neighbor , dist)
        
        for a,b,c in roads:
            graph[a].append((b,c))
            graph[b].append((a,c))
            
        min_score = float("inf")    
        visited = set()        
        q = deque([1])
        
        while q:
            curr = q.popleft()
            
            for dst, score in graph[curr]:
                if dst not in visited:
                    q.append(dst)
                    visited.add(dst)
                min_score = min(min_score, score)
                
        return min_score
        
        