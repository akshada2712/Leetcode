class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)
            
        path, visit = set(), set()
        output = []
        
        def dfs(src):
            if src in path:
                return False
            
            if src in visit:
                return True
            
            path.add(src)
            
            for nei in graph[src]:
                if dfs(nei) == False:
                    return False
            path.remove(src)
            visit.add(src)
            output.append(src)
            return True 
      
        for i in range(numCourses):
            if dfs(i) == False:
                return []
     
        return output
        