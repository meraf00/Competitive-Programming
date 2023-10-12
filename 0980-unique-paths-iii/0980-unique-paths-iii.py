class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        
        def get_nbrs(r, c):
            nbrs = []
            
            for dx, dy in directions:
                new_r = r + dy
                new_c = c + dx
                
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] != -1:
                        nbrs.append((new_r, new_c))
                            
            return nbrs                        
        
        visited = [[False] * cols for _ in range(rows)]
        
        path_count = 0
                        
        def dfs(r, c, visit_count): 
            nonlocal path_count
            
            if (r, c) == (end_row, end_col) and visit_count == non_obstacle_count:
                path_count += 1
                
            for nbr_r, nbr_c in get_nbrs(r, c):
                if visited[nbr_r][nbr_c]:
                    continue
                 
                visited[nbr_r][nbr_c] = True                
                dfs(nbr_r, nbr_c, visit_count + 1)  
                visited[nbr_r][nbr_c] = False                        
        
        start_row = start_col = None
        
        end_row = end_col = None
        
        non_obstacle_count = 0
        
        for r in range(rows):                            
            for c in range(cols):                                    
                if grid[r][c] == 1:
                    start_row, start_col = r, c
                
                if grid[r][c] == 2:
                    end_row, end_col = r, c
                    
                if grid[r][c] != -1:
                    non_obstacle_count += 1                
        
        visited[start_row][start_col] = True                
        
        dfs(start_row, start_col, 1)        
        
        return path_count
        
        
        
                
                
            