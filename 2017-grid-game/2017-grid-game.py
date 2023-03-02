class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:        
        cols = len(grid[0])
        
        # suffix sum on row 1
        # prefix sum on row 2
        for c in range(cols - 1):
            grid[0][~(c + 1)] += grid[0][~c]
            grid[1][c + 1] += grid[1][c]
        
        # to avoid if conditions when indexing        
        grid[0].append(0)                          
        grid[1].append(0)                          
        
        min_robot_2_pts = float("inf")        
        
        for c in range(cols):
            top_uncollected = grid[0][c + 1]
            
            bottom_uncollected = grid[1][c - 1]
            
            left_for_robot_2 = max(top_uncollected, bottom_uncollected)
            
            min_robot_2_pts = min(min_robot_2_pts, left_for_robot_2)        
        
        return min_robot_2_pts
        
        