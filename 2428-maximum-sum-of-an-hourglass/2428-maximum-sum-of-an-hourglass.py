class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        row_prefix = []
        
        for row in grid:
            new_row = [0] * n_cols         
            for cx, col in enumerate(row):
                if cx == 0:
                    new_row[cx] = col
                    continue
                new_row[cx] += new_row[cx-1] + col                 
            row_prefix.append(new_row)
                    
        max_sum = 0

        for r in range(n_rows - 2):
            top_row = row_prefix[r]
            mid_grid_row = grid[r + 1]
            bottom_row = row_prefix[r + 2]
            
            for c in range(2, n_cols):
                if c > 2:
                    top_sum = top_row[c] - top_row[c - 3]
                    bottom_sum = bottom_row[c] - bottom_row[c - 3]
                else:
                    top_sum = top_row[c]
                    bottom_sum = bottom_row[c]
                
                current_sum = top_sum + mid_grid_row[c - 1] + bottom_sum                
                max_sum = max(current_sum, max_sum)

        return max_sum


