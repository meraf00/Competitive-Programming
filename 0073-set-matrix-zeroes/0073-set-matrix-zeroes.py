class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_rows = set()
        zero_cols = set()
        for row_idx in range(rows):
            for col_idx in range(cols):
                if matrix[row_idx][col_idx] == 0:
                    zero_cols.add(col_idx)
                    zero_rows.add(row_idx)
        
        # convert the rows to zero
        for row_idx in zero_rows:
            matrix[row_idx] = [0] * cols
                
        for col_idx in zero_cols:
            for row_idx in range(rows):
                matrix[row_idx][col_idx] = 0
        
                