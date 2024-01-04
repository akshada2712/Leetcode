class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        visit = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i,j,0))
                    visit.add((i,j))
                    
#                 if grid[i][j] == 'X':
#                     visit.add((i,j))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]        
        while q:
            #print(q)
            row, col, res = q.popleft()
            
            for dr, dc in dirs:
                r, c = row + dr, col + dc
                
                if r >= 0 and r < m and c >= 0 and c < n:
                    #print(r,c,res,grid[r][c])
                    
                    if grid[r][c] == "#":
                        return res + 1 
                    
                    if grid[r][c] == "O":
                        q.append((r,c,res+1))
                        grid[r][c] = "X"
                        
        return -1
                    