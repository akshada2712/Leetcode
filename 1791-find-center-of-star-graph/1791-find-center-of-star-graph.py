class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = {n+1:[0,[]] for n in range(len(edges))}
        visit = set()
        
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        m = len(edges)
        for i in adj:
            if len(adj[i]) == m :
                return i
        