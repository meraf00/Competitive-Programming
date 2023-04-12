class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        
        def dfs(node):                        
            count = 0
            stack = [node]
            
            while stack:
                
                current_row, current_col = stack.pop()
                
                if grid[current_row][current_col] == 0:
                    continue
                    
                grid[current_row][current_col] = 0
                
                count += 1
                                        
                for nbr in get_neighbours((current_row, current_col)):
                    stack.append(nbr)
            
            return count
        
        
        def get_neighbours(node):
            row, col = node
            
            
            for dc, dr in directions:
                new_row = row + dr
                new_col = col + dc                                
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col]:
                    yield (new_row, new_col)
                                        
        
        max_area = 0
        for row in range(rows):
            for col in range(cols):                       
                if grid[row][col] != 0:
                    max_area = max(max_area, dfs((row, col)))
                
        
        return max_area