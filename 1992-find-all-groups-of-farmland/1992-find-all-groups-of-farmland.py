class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(row, col):
            nonlocal row2, col2
            visit[row][col] = 1
            row2 = max(row2, row)
            col2 = max(col2, col)
            
            for dr,dc in [(0,1), (0, -1), (1,0), (-1,0)]:
                nr, nc = dr + row, dc + col
                if 0 <= nr < len(land) and 0 <= nc < len(land[0]) and land[nr][nc] == 1 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    dfs(nr, nc)
                    
        ans = []
        visit = [[0] * len(land[0]) for _ in range(len(land))]
        
        for r1 in range(len(land)):
            for c1 in range(len(land[0])):
                if land[r1][c1] == 1 and visit[r1][c1] == 0:
                    row2, col2 = 0, 0
                    dfs(r1, c1)
                    ans.append([r1, c1, row2, col2])
                    
        return ans