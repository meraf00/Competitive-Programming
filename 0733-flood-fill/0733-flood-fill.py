class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        source_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        
        # visited = set()
        
        def dfs(node):
            r, c = node
            image[r][c] = -1 # color
            
            for nbr in get_neighbours(node):                
                dfs(nbr)
        
        def get_neighbours(node):
            row, col = node
            
            neighbours = []
            
            for direction in directions:
                y, x = direction
                
                new_row = row + y
                new_col = col + x
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if image[new_row][new_col] == source_color:
                        neighbours.append((new_row, new_col))
            
            return neighbours
        
        dfs((sr, sc))
        
        # fill
        for r in range(rows):
            for c in range(cols):
                if image[r][c] == -1:
                    image[r][c] = color
        
        return image
            
            
            
            