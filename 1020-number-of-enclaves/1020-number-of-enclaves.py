class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            
            if not grid[r][c] or (r,c) in visit:
                return 0
            
            visit.add((r,c))
            
            res = 1 
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in dirs:
                res += dfs(r + dr, c + dc)
            return res
        
        land, bLand = 0, 0
        for r in range(rows):
            for c in range(cols):
                land += grid[r][c]
                #new_land 
                if (grid[r][c] and (r,c) not in visit) and (c in [0,cols-1] or r in [0,rows-1]):
                    bLand += dfs(r,c)
                    
        return land - bLand
        
        
        
        
        
#         rows = len(grid)
#         cols = len(grid[0])
        
#         def dfs(r,c):
#             # print(r,c,grid[r][c],rows,cols,visit)
#             # if (r==rows or c ==cols): print('1')
#             # elif (r<0 or c < 0): print('2')
#             # elif (not grid[r][c]): print('3')
#             # elif ((r,c) in visit): print('4')
                
#             if (r < rows or c < cols or 
#                 r == rows or c == cols or 
#                 not grid[r][c] or (r,c) in visit):
#                 #print('in')
#                 return 0         
#             visit.add((r,c))
#             #print('added')
#             res = 1
#             #print('resini',res)
#             dirs = [[0,1],[0,-1],[1,0],[-1,0]]
#             for dr, dc in dirs:                
#                 res += dfs(r + dr, c + dc)            
#             #print('res',res)
#             return res               
#         land, bLand = 0, 0
#         visit = set()
#         for i in range(rows):
#             for j in range(cols):
#                 land += grid[i][j] 
#                 #print(land)
#                 if (grid[i][j] and (i,j) not in visit and (j in [0,cols-1] or i in [0,rows-1])):
#                     #print('f',i,j)
#                     bLand += dfs(i,j)  
#                     #print('f',bLand)
        
        
#         #print(land, bLand)
#         return land - bLand 
        