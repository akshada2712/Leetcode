class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visit = set()
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visit or grid[r][c] == 0:
                    return 0
            visit.add((r,c))
            f = grid[r][c]
            
            dirs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            
            for dr, dc in dirs:
                
                f += dfs(dr,dc)
                
            return f
            
            
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] :
                    cnt  = max(cnt, dfs(i,j))
        return cnt
                    
        