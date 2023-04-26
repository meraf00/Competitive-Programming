class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),            
        ]
        
        rows = len(board)
        cols = len(board[0])
        
        def get_neighbours(coord):
            row, col = coord
            
            neighbours = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != "B":
                    neighbours.append((new_row, new_col))
                
            
            return neighbours
                    
        
        def dfs(node):
            row, col = node
            
            if board[row][col] != "E":
                return
            
            board[row][col] = "B"
            
            mine_count = 0
            next_ = []
            for nbr in get_neighbours(node):
                nbr_row, nbr_col = nbr
                
                if board[nbr_row][nbr_col] == "M":
                    mine_count += 1
                    continue
                    
                next_.append(nbr)
                
            
            if mine_count == 0:
                for nbr in next_:                
                    dfs(nbr)
                
            else:                
                board[row][col] = str(mine_count)
            
          
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
            
        dfs(click)
        
        return board
        