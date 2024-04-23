class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            
            for nei in graph[i]:
                dfs(nei)
                
            return True
            
            
            
        visit = set()
        cnt = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                cnt += 1
                
        return cnt 