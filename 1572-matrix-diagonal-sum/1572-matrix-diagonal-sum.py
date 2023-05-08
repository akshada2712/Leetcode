class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        tot = 0
        visit = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j and (i,j) not in visit:
                    visit.add((i,j))
                    tot += mat[i][j]
                elif i + j == len(mat) - 1 and (i,j) not in visit:
                    visit.add((i,j))
                    tot += mat[i][j]
                    
        return tot
                    
        