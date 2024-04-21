class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        # approach 2 -using bfs
        
        graph = collections.defaultdict(list)
        
        
        # as it is bidirectional
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        q = collections.deque()
        seen = set()
        q.append(source)
        seen.add(source)
        
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            
            for nei in graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return False
        
        
        
        # approach 1 - using dfs
        
#         # use dfs 
#         # create a graph 
        
#         graph = collections.defaultdict(list)
        
        
#         # as it is bidirectional
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
            
#         seen = set()
#         #print(graph)
#         def dfs(src):
           
#             if src == destination:
#                 return True
            
#             if src not in seen:
#                 seen.add(src)
#                 for nei in graph[src]:
#                     if dfs(nei):
#                         return True
                    
#             return False
        
#         return dfs(source)
           
            
                
#         dfs(source)
        