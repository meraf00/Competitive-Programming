class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        rows = len(grid)
        cols = len(grid[0])
        
        def get_neigbours(coord):
            row, col = coord
            
            neighbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == FRESH:
                    neighbours.append((new_row, new_col))
            
            return neighbours
        
        def bfs(start_coords):
            queue = deque(map(lambda x: (x, 0), start_coords))
            
            max_level = 0
            
            while queue:                
                current, level = queue.popleft()                                
                                    
                max_level = max(max_level, level)
                
                for nbr in get_neigbours(current):                    
                    queue.append((nbr, level + 1))
                    r, c = nbr
                    grid[r][c] = ROTTEN
            
            return max_level
        
        
        rotten_coords = []
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == ROTTEN:
                    rotten_coords.append((row, col))
        
        time = bfs(rotten_coords)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == FRESH:
                    return -1
        
        return time
        
        
            
            
                
                