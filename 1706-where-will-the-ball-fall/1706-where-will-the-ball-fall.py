class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [i for i in range(cols)]
        
        for r in range(rows):
            for ball in range(cols):
                if dp[ball] == -1:
                    continue
                
                curr_col = dp[ball]
                
                if (grid[r][curr_col] == 1 and curr_col == cols - 1) or (
                    curr_col + 1 < cols and grid[r][curr_col] == 1 and grid[r][curr_col + 1] == -1
                ):
                    dp[ball] = -1
                
                elif (grid[r][curr_col] == -1 and curr_col == 0) or (
                    curr_col - 1 >= 0 and grid[r][curr_col] == -1 and grid[r][curr_col - 1] == 1
                ):
                    dp[ball] = -1
                    
                else:
                    dp[ball] += grid[r][curr_col]
              
        return dp