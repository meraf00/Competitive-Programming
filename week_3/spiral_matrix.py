from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:        
        
        rows, cols = len(matrix), len(matrix[0])
        
        output = [0] * (rows * cols)
                
        direction = "r"
        
        i = 0
        start_row, end_row, start_col, end_col = 0, rows, 0, cols
        
        while i < len(output):                         
            if direction == "r":                
                for c in range(start_col, end_col):
                    output[i] = matrix[start_row][c]
                    i += 1
                direction = "d" 
                start_row += 1                
            
            elif direction == "d":                
                for r in range(start_row, end_row):
                    output[i] = matrix[r][end_col - 1]
                    i += 1
                direction = "l"
                end_col -= 1
            
            elif direction == "l":
                for c in range(end_col - 1, start_col - 1, -1):
                    output[i] = matrix[end_row - 1][c]
                    i += 1
                direction = "u"
                end_row -= 1
            
            elif direction == "u":
                for r in range(end_row - 1, start_row - 1, -1):
                    output[i] = matrix[r][start_col]
                    i += 1
                direction = "r"
                start_col += 1            
                
        return output        