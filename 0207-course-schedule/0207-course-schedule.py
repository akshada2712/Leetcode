class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        
        visited = set()
        
        for a,b in prerequisites:
            graph[b].append(a)
        
        def dfs(src):
            if src in visited:
                return False            
            if graph[src] == []:
                return True
            
            visited.add(src)
            
            for i in graph[src]:
                if not dfs(i):
                    return False
            
            visited.remove(src)
            graph[src] = []
            return True
        
        for i in range(numCourses-1):
            if not dfs(i): return False
        return True
                
            
            
        