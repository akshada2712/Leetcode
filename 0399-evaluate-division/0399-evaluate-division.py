class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (x,y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1/v
        
        
        def dfs(x,y,visit):
            if x not in graph or y not in graph:
                return -1
            
            if y in graph[x]:
                return graph[x][y]
            
            for nei in graph[x]:
                if nei not in visit:
                    visit.add(nei)
                    temp = dfs(nei,y,visit)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][nei] * temp
                    
            return -1
        
        ans = []
        
        for i,j in queries:
            ans.append(dfs(i,j,set()))
            
        return ans
                    
            