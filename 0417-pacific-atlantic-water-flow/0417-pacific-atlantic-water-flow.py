class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return
        
        ROWS, COLS = len(heights), len(heights[0])
        
        pv = [[False] * COLS for _ in range(ROWS)]
        av = [[False] * COLS for _ in range(ROWS)]
        
        pq= deque()
        aq = deque()
        
        for i in range(COLS):
            pv[0][i] = True
            pq.append((0,i))
            av[ROWS-1][i] = True
            aq.append((ROWS - 1, i))
            
        for i in range(ROWS):
            pv[i][0] = True
            pq.append((i,0))
            av[i][COLS-1] = True
            aq.append((i,COLS-1))
            
        def bfs(visit, queue):
            dirs = [[0,1],[0,-1],[-1,0],[1,0]]
            while queue:
                r,c = queue.popleft()
                
                for dr, dc in dirs:
                    row = dr + r
                    col = dc + c
                    
                    if 0 <= row < ROWS and 0 <= col < COLS and not visit[row][col]:
                        if heights[row][col] >= heights[r][c]:
                            visit[row][col] = True
                            queue.append((row,col))
                            
                            
        bfs(av, aq)
        bfs(pv, pq)
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if pv[i][j] and av[i][j]:
                    res.append([i,j])
                    
        return res
                
                
            
        