class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:        
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def get_nbrs(row, col):
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == grid[row][col]:
                    nbrs.append((new_row, new_col))
            
            return nbrs
        
        
        def has_cycle(row, col):
            stack = [(row, col, None)]
            
            while stack:
                r, c, parent = stack.pop()
                
                visited[r][c] = True
                
                for nbr_r, nbr_c in get_nbrs(r, c):
                    if (nbr_r, nbr_c) == parent:
                        continue
                    
                    if visited[nbr_r][nbr_c]:                        
                        return True
                    
                    stack.append((nbr_r, nbr_c, (r, c)))
            
            return False
                                            
        
        visited = [[False] * cols for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col]:                    
                    if has_cycle(row, col):                        
                        return True
        
        return False