class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:        
        rows = len(grid2)
        cols = len(grid2[0])
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
                
        
        def dfs(node):
            r, c = node
            
            is_subisland = grid1[r][c] == 1            
            
            grid2[r][c] = 0 # mark as visited                        
            
            for nbr in get_neighbours(node):                 
                is_subisland = dfs(nbr) and is_subisland
            
            return is_subisland
                        
        
        def get_neighbours(node):
            row, col = node
            
            neighbours = []
            
            for direction in directions:
                y, x = direction
                
                new_row = row + y
                new_col = col + x
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid2[new_row][new_col] == 1:
                        neighbours.append((new_row, new_col))
            
            return neighbours
        
        counter = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    if dfs((row, col)):
                        counter += 1                            
        
        return counter