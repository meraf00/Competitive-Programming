class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        def get_nbrs(row, col):
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if land[new_row][new_col] == 1:
                        nbrs.append((new_row, new_col))
            
            return nbrs
        
        
        def dfs(row, col):
            stack =[(row, col)]
            
            br, bc = row, col
            
            while stack:
                c_row, c_col = stack.pop()
                
                # mark as visited
                land[c_row][c_col] = 0
                
                br = max(c_row, br)
                bc = max(c_col, bc)
                
                for nbr in get_nbrs(c_row, c_col):
                    stack.append(nbr)
            
            return br, bc
        
            
        groups = []
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1:
                    br, bc = dfs(row, col)
                    groups.append((row, col, br, bc))
                        
        return groups
    
    
    
    
    
    
    
    
                