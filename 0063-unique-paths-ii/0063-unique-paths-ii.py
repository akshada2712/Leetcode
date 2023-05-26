class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        memo = {(M-1, N - 1): 1}
        
        def dfs(r,c):
            if r == M or c == N or obstacleGrid[r][c]:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return memo[(r,c)]

        return dfs(0,0)