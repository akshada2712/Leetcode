class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # use dfs 
        # create a graph 
        
        graph = collections.defaultdict(list)
        
        
        # as it is bidirectional
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        seen = set()
        #print(graph)
        def dfs(src):
           
            if src == destination:
                return True
            
            if src not in seen:
                seen.add(src)
                for nei in graph[src]:
                    if dfs(nei):
                        return True
                    
            return False
        
        return dfs(source)
           
            
                
        dfs(source)
        