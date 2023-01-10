class Solution:
    def transpose(self, matrix, rows, cols):        
        for row in range(rows):
            for col in range(cols):
                if row > col:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
    def reverse_rows(self, matrix, rows, cols):
        for row in range(rows):
            for col in range(cols // 2):
                matrix[row][col], matrix[row][cols-col-1] = matrix[row][cols-col-1], matrix[row][col]
                

        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.transpose(matrix, rows, cols)
        self.reverse_rows(matrix, rows, cols)
        
        
        