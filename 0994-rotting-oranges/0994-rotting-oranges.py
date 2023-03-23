from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = Queue()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.put([r,c])
                    
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        while q.qsize() > 0 and fresh > 0:
            for i in range(q.qsize()):
                r,c = q.get()

                for dr, dc in dirs:
                    rows = dr + r
                    cols = dc + c

                    if rows < 0 or cols < 0 or rows >= ROWS or cols >= COLS or grid[rows][cols] != 1:
                        continue
                    grid[rows][cols] = 2
                    q.put([rows,cols])
                    fresh -= 1

            time += 1
            
        return time if fresh == 0 else -1
                    
        
        