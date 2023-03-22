class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        def helper(r,c):
            
            if r > len(grid)-1 or r < 0 or c > len(grid[0])-1 or c < 0:
                return 
            
            if grid[r][c] == '0':
                return False
            
            pos = str(r) + '-' + str(c)
            if pos in visited:
                return
            
            visited.add(pos)
            
            helper(r+1,c)
            helper(r-1,c)
            helper(r,c+1)
            helper(r,c-1)
            
            return True
        
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if helper(i,j):
                    cnt += 1
                    
        return cnt
        