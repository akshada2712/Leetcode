class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N
        
        visit = set()
        
        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return
            
            visit.add((r,c))
            
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
                
        def bfs():
            res, q = 0, deque(visit)
            
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]: return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                res += 1
         
            
            
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)     # fill visit set for 1st island
                    return bfs()
                    
                
            
        
        