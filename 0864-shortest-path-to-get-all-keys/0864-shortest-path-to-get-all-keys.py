# ["@..aA",".bB#.","....."]
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        WALL = "#"
        OPEN = "."        
        
        def is_key(coord):
            row, col = coord
            return grid[row][col].isalpha() and grid[row][col].islower()
        
        def is_lock(coord):
            row, col = coord
            return grid[row][col].isalpha() and grid[row][col].isupper()
        
        
        def is_unlockable(lock, keys):
            row, col = lock
            
            key = grid[row][col].lower()
            
            key_idx = key_map[key]
            
            return keys & (1 << key_idx)
        
        def get_neighbours(coord, keys):
            row, col = coord          
            neighbours = []
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx                                
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != WALL:
                    nbr = (new_row, new_col)
                    if is_lock(nbr) and not is_unlockable(nbr, keys):
                        continue
                    neighbours.append((new_row, new_col))
            
            return neighbours
                                                
        key_map = {}
        start_pos = None
        for row in range(rows):
            for col in range(cols):
                if is_key((row, col)):
                    key = grid[row][col]
                    if key not in key_map:
                        key_map[key] = len(key_map)
                elif grid[row][col] == "@":
                    start_pos = (row, col)
                    
        target = 0
        
        for v in key_map.values():
            target = target | (1 << v)
                    
        
        visited = defaultdict(set)
        
        visited[0].add(start_pos)
        
        # (start_pos, keys, path_length)
        queue = deque([(start_pos, 0, 0)])
        
        min_distance = float('inf')

        while queue:
            current, keys, path_length = queue.popleft()
            
            if target == keys: 
                min_distance = min(path_length, min_distance)

            
            for nbr in get_neighbours(current, keys):  

                
                if nbr not in visited[keys]:
                    visited[keys].add(nbr)
                    
                    nbr_row, nbr_col = nbr
                    if is_key(nbr):                        
                        key = grid[nbr_row][nbr_col]
                        nbr_keys = keys | (1 << key_map[key])
                    else:
                        nbr_keys = keys
                    
                    visited[nbr_keys].add(nbr)                    
                    queue.append((nbr, nbr_keys, path_length + 1))
                    
                    
        
        if min_distance == float('inf'):
            return -1
        
        return min_distance
                    
      