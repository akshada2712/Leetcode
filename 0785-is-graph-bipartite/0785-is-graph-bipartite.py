import collections
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        
        for node in range(len(graph)):
            if node not in visited:
                q = collections.deque([(node,1)])

                while q:
                    node, color = q.popleft()

                    if node in visited:
                        if visited[node] == color:
                            continue
                        else:
                            return False

                    visited[node] = color
                    for nei in graph[node]:
                        q.append((nei,color * (-1)))
                    
        return True
        