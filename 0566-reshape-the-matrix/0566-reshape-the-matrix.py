class Solution:
    def isReshapeLegal(self, original_rows, original_cols, 
                       reshape_rows, reshape_cols):        
        return original_rows * original_cols == reshape_rows * reshape_cols 
    
    
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        
        if not self.isReshapeLegal(rows, cols, r, c):
            return mat
        
        new_mat = [[0] * c for _ in range(r)]
        
        total_elements = rows * cols                
        
        for index in range(total_elements):
            original_row_idx = index // cols
            original_col_idx = index % cols
            reshaped_row_idx = index // c
            reshaped_col_idx = index % c                        
            
            original = mat[original_row_idx][original_col_idx]
            new_mat[reshaped_row_idx][reshaped_col_idx] = original
        
        return new_mat
        
        
        
        
        