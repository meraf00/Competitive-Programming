class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        target = (rows - 1, cols - 1)
        
        directions = {
            1: [(-1, 0), (1, 0)],
            2: [(0, -1), (0, 1)],
            3: [(-1, 0), (0, 1)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(1, 0), (0, -1)]
        }
        
        
        def get_complement(x, y):
            return (-x, -y)
            
        
        def get_nbrs(row, col):
            nbrs = []
            
            road_type = grid[row][col]
            
            for dx, dy in directions[road_type]:
                nbr_r = row + dy
                nbr_c = col + dx
                
                if 0 <= nbr_r < rows and 0 <= nbr_c < cols:
                    
                    nbr_road_type = grid[nbr_r][nbr_c]
                                        
                    if get_complement(dx, dy) in directions[nbr_road_type]:
                        nbrs.append((nbr_r, nbr_c))
            
            return nbrs
        
        
        stack = [(0, 0)]
        visited = set()
        
        while stack:
            curr_r, curr_c = stack.pop()
            
            visited.add((curr_r, curr_c))
            
            if (curr_r, curr_c) ==  target:
                return True
                        
            for nbr_r, nbr_c in get_nbrs(curr_r, curr_c):                
                if (nbr_r, nbr_c) in visited:
                    continue
                stack.append((nbr_r, nbr_c))
        
        return False