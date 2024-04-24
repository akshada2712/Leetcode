class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        
        # we are using kind of topological sort 
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        edge_cnt = {}
        leaves = deque()
        
        # counting the indegree for every node
        # if indegree is 1 which means it is leaf node 
        # hence add to leaves 
        # we would be doing layerwise bfs 
        for src, nei in adj.items():
            if len(nei) == 1:
                leaves.append(src)
            edge_cnt[src] = len(nei)
            
            
        # layerwise bfs
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                
                for nei in adj[node]:
                    
                    # removing edge 
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
                
                
            
        