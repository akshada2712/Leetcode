class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i:[] for i in range(n)}
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(cur, par):
            time = 0
            for child in graph[cur]:
                if child == par:
                    continue
                childTime = dfs(child, cur)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        
        return dfs(0,-1)