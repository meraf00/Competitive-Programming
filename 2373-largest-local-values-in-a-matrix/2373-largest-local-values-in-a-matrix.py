class Solution:    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        max_local = [[0] * (cols - 2) for _ in range(rows - 2)]
        
        
        for row_idx in range(rows - 2):
            for col_idx in range(cols - 2):
                max_val = float("-inf")
                for rx in range(3):
                    for cx in range(3):
                        max_val = max(max_val, grid[row_idx + rx][col_idx + cx])
                
                max_local[row_idx][col_idx] = max_val
        
        return max_local
                
        