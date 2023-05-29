class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n,q,visit = len(mat), len(mat[0]), deque(), set()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
                else:
                    mat[i][j] = -1
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]            
        while q:
            r,c = q.popleft()
            
            for dr, dc in dirs:
                i,j = r + dr, c + dc
                if 0 <= i < m and 0 <= j < n and (i,j) not in visit:
                    mat[i][j] = mat[r][c] + 1
                    q.append((i,j))
                    visit.add((i,j))
                    
        return mat
                    
        