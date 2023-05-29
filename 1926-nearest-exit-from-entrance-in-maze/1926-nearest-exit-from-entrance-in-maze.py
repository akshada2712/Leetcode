class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visit = set()
        m = len(maze)
        n = len(maze[0])      
        
        q = deque([(entrance[0], entrance[1], 0)])
        
        maze[entrance[0]][entrance[1]] = '+'
        
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        
        while q:
            r,c,cnt = q.popleft()
            if (r == 0 or c == 0 or r == m -1 or c == n -1 ) and [r,c] != entrance:
                return cnt
            
            for dr, dc in dirs:
                i = r + dr
                j = c + dc
                
                if 0 <= i < m and 0 <= j < n and maze[i][j] == '.':
                    
                    maze[i][j] = '+'
                    
                    q.append((i,j,cnt+1))
                    
        return -1
                