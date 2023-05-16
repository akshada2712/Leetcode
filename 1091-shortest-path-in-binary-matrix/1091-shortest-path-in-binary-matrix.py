class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        N = len(grid)
        q = deque([(0,0,1)])  # row, col ,length
        
        dirs = [[0,1],[0,-1],[-1,0],[1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        
        visit = set()
        
        while q:
            row, col, res = q.popleft()  
            if min(row,col) < 0 or max(row,col) >= N or grid[row][col]:
                continue
                
            if row == N - 1 and col == N -1:
                return res
            
            for dr, dc in dirs:
                r , c = row + dr, col + dc
                
                if (r,c) not in visit:
                    q.append((r,c,res + 1))
                    visit.add((r,c))
                
        return -1
            
            
        