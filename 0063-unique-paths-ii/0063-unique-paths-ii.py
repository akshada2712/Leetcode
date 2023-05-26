class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #dp solution
        
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [0] * N
        dp[N-1] = 1
        
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:  
                    dp[c] = dp[c] + dp[c + 1]
                # else:      this case not req
                #     dp[c] = dp[c] + 0
                
        return dp[0]
                    
                
        
        
        
        # recursive solution
#         M = len(obstacleGrid)
#         N = len(obstacleGrid[0])
#         memo = {(M-1, N - 1): 1}
        
#         def dfs(r,c):
#             if r == M or c == N or obstacleGrid[r][c]:
#                 return 0
#             if (r,c) in memo:
#                 return memo[(r,c)]
            
#             memo[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
#             return memo[(r,c)]

#         return dfs(0,0)