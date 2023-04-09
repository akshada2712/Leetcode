class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        path = set()
        adj =defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            
        # return max freq of color
        
        def dfs(node):            
            if node in path:
                return float("inf")
            
            if node in visit:
                return 0           
            
            
            visit.add(node)
            path.add(node)
            colorIdx = ord(colors[node]) - ord('a')            
            count[node][colorIdx] = 1
            
            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")                
                for c in range(26):
                    count[node][c] = max(count[node][c], (1 if c == colorIdx else 0) + count[nei][c]) 
            
            path.remove(node)
            return max(count[node])
        
        res = 0
        n = len(colors)
        visit, path = set(), set()
        count = [[0] * 26 for i in range(len(colors))]  #map count[node][color] -> max freq color
        for i in range(len(colors)):
            res = max(dfs(i),res)
            
        return -1 if res == float("inf") else res