class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        
        north = [0] * cols               
        west  = [0] * rows        
        
        for idx, row in enumerate(grid):
            west[idx] = max(row)
        
        for col in range(cols):
            for row in range(rows):
                north[col] = max(grid[row][col], north[col])                                
        
        change = 0
        
        for row in range(rows):
            for col in range(cols):
                new_height = min(west[row], north[col])
                change += new_height - grid[row][col]
                grid[row][col] = new_height
                        
        return change
        
        