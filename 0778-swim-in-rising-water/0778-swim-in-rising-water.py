class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        target_node = (rows-1, cols-1)
        
        priority_queue = [(grid[0][0], 0, 0)]
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]                  
        
        grid[0][0] = -1
        
        while priority_queue:
            cost, r, c = heappop(priority_queue)
                        
            if (r, c) == target_node:
                return cost                                       
            
            for dx, dy in directions:
                nbr_r = r + dy
                nbr_c = c + dx
                if 0 <= nbr_r < rows and 0 <= nbr_c < cols:
                    if grid[nbr_r][nbr_c] != -1:               
                        heappush(priority_queue, (max(cost, grid[nbr_r][nbr_c]), nbr_r, nbr_c))
                        grid[nbr_r][nbr_c] = -1
                