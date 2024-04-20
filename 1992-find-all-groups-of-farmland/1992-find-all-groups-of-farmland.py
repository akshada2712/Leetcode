class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        # approach:
        
        # visit -> initalize to 0 same as land if that row, col is visited mark 1 to avoid revisting
        # row2, col2 -> indicate the right bottom corners they would always be maximum hence we create new rows, cols idx we would be replacing them with maximum values
        # marking nodes as 1 in visit 
        # run dfs in 4 direction
        # once dfs ends you would be having ro2, col2 
        # while running 1st for loop we would be initializing our r1, c1 i.e top left corners
        # append in our answers
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