class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1)            
        ]
        
        rows = len(grid)
        cols = len(grid[0])
        
        def get_neighbours(coord):
            row, col = coord
            
            neighbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx                                
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:
                    neighbours.append((new_row, new_col))
            
            return neighbours
                
        
        queue = deque([((-1, -1), 0)])        
        
        target = (rows - 1, cols - 1)
        
        while queue:            
            current_cell, length = queue.popleft()
            
            if current_cell == target:
                return length
            
            for nbr in get_neighbours(current_cell):
                # mark as visited
                row, col = nbr                
                grid[row][col] = 1
                
                queue.append((nbr, length + 1))
        
        return -1
                
                        
            
        