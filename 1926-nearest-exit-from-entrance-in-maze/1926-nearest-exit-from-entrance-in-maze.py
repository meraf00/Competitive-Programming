class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        rows = len(maze)
        cols = len(maze[0])
        
        def isExit(coord):
            if coord == entrance:
                return False
            
            row, col = coord
            
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                return True
            
            return False
            
        
        def get_neighbours(coord):
            row, col = coord
            
            neighbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.':
                    neighbours.append((new_row, new_col))
                    
            return neighbours
        
        
        row, col = entrance
        maze[row][col] = '+'
        
        queue = deque([(entrance, 0)])                
        
        while queue:
            current, distance = queue.popleft()
            
            if isExit(current):
                return distance
            
            for nbr in get_neighbours(current):
                row, col = nbr
                maze[row][col] = '+'
                queue.append((nbr, distance + 1))
        
        return -1
        