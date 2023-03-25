class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = True
            res = 1
            for nbr in graph[node]:
                res += dfs(nbr)
                
            return res
        
        graph = {}
        for i in range(n):
            graph[i] = []
            
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [False for _ in range(n)]
        compo = []
        for node in range(n):
            if visited[node] == False:
                compo.append(dfs(node))
                
        ans = n * (n-1) // 2
        for k in compo:
            ans -= k * (k-1)//2
            
        return ans
        
        
#         graph = {i:[] for i in range(n)}
#         visit = set()
#         for a,b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#             key = ((a,b))
#             visit.add(key)
#         unvisit = set()
#         #print(visit) 
#         cnt = 0
#         for i in range(n):
#             for j in range(i+1,n):
#                 key = (i,j)
#                 if key not in visit:
#                     unvisit.add(key)
#                     cnt += 1
                    
#         print("visit",visit)
#         print("unvisit",unvisit)
                    
#         return cnt
                
# #         for i in range(n):
# #             for node in graph[i]:
                
        