class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        target_node = (rows-1, cols-1)
        
        priority_queue = [(grid[0][0], (0, 0))]
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        
        def get_neighbours(node):
            row, col = node
            
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] != -1:
                        nbrs.append((new_row, new_col))
                
            return nbrs                
        
        
        while priority_queue:
            cost, current_node = heappop(priority_queue)
            
            if current_node == target_node:
                return cost       
            
            for nbr in get_neighbours(current_node):
                r, c = nbr
                weight = grid[r][c]
                grid[r][c] = -1

                heappush(priority_queue, (max(cost, weight), nbr))                        