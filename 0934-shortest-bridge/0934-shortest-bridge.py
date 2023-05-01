class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        def get_neighbours(coord):
            row, col = coord
            
            neighbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                neighbours.append((new_row, new_col))
            
            return neighbours
    
        def is_inbound(coord):
            row, col = coord
            return 0 <= row < rows and 0 <= col < cols
        
        
        queue = deque()                
                
        for row in range(rows):            
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    grid[row][col] = 2
                    break
                    
            if grid[row][col] == 2:
                break
        
        borders = set()
        
        while queue:
            current = queue.popleft()
            
            for nbr in get_neighbours(current):
                r, c = nbr
                if is_inbound(nbr) and grid[r][c] == 1:
                    grid[r][c] = 2
                    queue.append(nbr)
                
                if is_inbound(nbr) and grid[r][c] == 0:
                    borders.add(current)
        
        
        queue = deque(map(lambda coord: (coord, 0), borders))                
        
        
        min_distance = float('inf')
        
        while queue:
            current, distance = queue.popleft()
            
            for nbr in get_neighbours(current):
                r, c = nbr
                if is_inbound(nbr) and grid[r][c] == 0:
                    grid[r][c] = 2
                    queue.append((nbr, distance + 1))
                
                if is_inbound(nbr) and grid[r][c] == 1:
                    
                    min_distance = min(min_distance, distance)
        
        
        return min_distance
                    
        
                
        
                    
                    
        