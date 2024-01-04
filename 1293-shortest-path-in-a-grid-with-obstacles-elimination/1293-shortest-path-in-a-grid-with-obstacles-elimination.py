class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(grid)
        n = len(grid[0])
        target = (m-1,n-1)
        
        state = (0,0,k)
        q = deque([(0,state)]) # steps, state
        visit = set((state))
        
        
        while q:
            steps, (row,col,k) = q.popleft()
            
            if (row,col) == target:
                return steps
            
            for dr, dc in dirs:
                r,c = dr + row, dc + col
                 
                if (0 <= r < m) and (0 <= c < n):
                    newElim = k - grid[r][c]
                    newState = (r,c,newElim)
                    
                    if newElim >= 0 and newState not in visit:
                        visit.add((newState))
                        q.append((steps+1, newState))
                        
        return -1