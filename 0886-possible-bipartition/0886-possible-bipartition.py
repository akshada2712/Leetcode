class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(n+1)]
        for k in dislikes:
            adj[k[0]].append(k[1])
            adj[k[1]].append(k[0])
            
        #print(adj)
        def bfs(src):
            q = deque([src])
            col[src] = 0
            
            while q:
                node = q.popleft()
                
                for nei in adj[node]:
                    if col[nei] == col[node]:
                        return False
                    if col[nei] == -1:
                        col[nei] = 1 - col[node]
                        q.append(nei)
                        
            return True
        
        col = [-1] * (n+1)
        
        for i in range(1,n+1):
            if col[i] == -1:
                if not bfs(i):
                    return False
            
        return True
                    