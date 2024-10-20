class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l , r = 0, len(matrix) - 1
        
        while l < r : 
            for i in range(r - l):
                top, bottom = l, r    # sqaure matrix
                
                #save topleft
                topLeft = matrix[top][l + i]
                
                # move bottom left in topleft
                matrix[top][l + i] = matrix[bottom - i][l]
                
                #move bottom right in bottomleft
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move topright in bottomright
                matrix[bottom][r - i] = matrix[top + i][r]
                
                #move topleft into topright
                matrix[top + i][r] = topLeft
                
            l += 1
            r -= 1
        return matrix