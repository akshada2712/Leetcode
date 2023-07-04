class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        # change -> 1 : 2
        # change -> 0 to -1
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        
        for i in range(m):
            for j in range(n):
                liveCnt = 0
                for dr, dc in dirs:
                    r = dr + i
                    c = dc + j
                    
                    if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                        liveCnt += 1
                if board[i][j] == 1:
                    if liveCnt < 2 or liveCnt > 3:
                        board[i][j] = -1
                elif liveCnt == 3:
                    board[i][j] = 2
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
                