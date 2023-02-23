class Solution:    
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        prefix_sum = [[0] * (cols+1) for _ in range(rows+1)]
        
        for row in range(rows):
            for col in range(cols):
                prefix_sum[row+1][col+1] = prefix_sum[row][col+1] + prefix_sum[row+1][col] - prefix_sum[row][col] + matrix[row][col]
            
        block_sum = [[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                row1 = max(0, r - k)
                col1 = max(0, c - k)
                row2 = min(rows-1, r + k)
                col2 = min(cols-1, c + k)
                block_sum[r][c] = prefix_sum[row2+1][col2+1] - prefix_sum[row2+1][col1] - prefix_sum[row1][col2+1] + prefix_sum[row1][col1]
        
        return block_sum
        
        
        
        
        
        
        
        