class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        diagonal_elements = {}
        
        for row_idx in range(rows):
            for col_idx in range(cols):
                diagonal_id = row_idx - col_idx
                
                if diagonal_id in diagonal_elements:
                    if diagonal_elements[diagonal_id] != matrix[row_idx][col_idx]:
                        return False
                
                else:
                    diagonal_elements[diagonal_id] = matrix[row_idx][col_idx]
        
        return True