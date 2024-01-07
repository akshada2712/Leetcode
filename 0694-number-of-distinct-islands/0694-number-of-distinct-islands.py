class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c):
            #print(r,c)
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if (r,c) in seen or not grid[r][c]:
                return
            seen.add((r,c))
            currIsland.add((r - rowOrigin, c - colOrigin))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            
        seen = set()
        uniIslands = set()
        for row in range(m):
            for col in range(n):
                
                currIsland = set()
                rowOrigin = row
                colOrigin = col
                
                dfs(row,col)
                if currIsland:
                    
                    uniIslands.add(frozenset(currIsland))
                    
        return len(uniIslands)
        