class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        cache = {}
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        def helper(r,c):
            if r >= rows or c >= cols:
                return 0 
            
            if (r,c) not in cache:
                down = helper(r + 1, c)
                diag = helper(r +1, c+ 1)
                left = helper(r, c + 1)
                cache[(r,c)] = 0
                
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(left, diag, down)
                
            return cache[(r,c)]
        
        helper(0,0)
        
        return max(cache.values()) ** 2
            
        
#         dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
#         step = 0
#         area = 0
        
#         for i in range(len(matrix) - 1, -1, -1):
#             for j in range(len(matrix[0]) -1, -1, -1):
#                 if matrix[i][j] == 1:
#                     step += 1
#                     area = max(area, step ** 2)
                    
        
#         print(dp)