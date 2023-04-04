class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0])-1
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        while l <= r:
            for i in range(len(matrix[0])):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                
            r -= 1
            l += 1