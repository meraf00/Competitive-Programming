class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),            
            (-1, 0)
        ]
        
        
        rows = len(board)
        cols = len(board[0])
                
        
        def get_neigbours(coord):
            row, col = coord
            
            neigbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row <= rows and 0 <= new_col <= cols and board[new_row][new_col] == "O":
                    neigbours.append((new_row, new_col))
            
            return neigbours
        
    
        
        def isEdge(coord):
            row, col = coord            
            return row == 0 or col == 0 or row == rows - 1 or col == cols - 1
            
        
        
        def dfs(coord, visited = None):
            if visited == None:
                visited = set()
                
            visited.add(coord)   
            
            if isEdge(coord):
                return
            
            
            for nbr in get_neigbours(coord):
                if nbr in visited:
                    continue
                
                if not dfs(nbr, visited):
                    return
            
            return visited
                
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    
                    is_surrounded = dfs((row, col))
                    
                    if is_surrounded:
                        for r, c in is_surrounded:
                            board[r][c] = "X"
                        
        
        