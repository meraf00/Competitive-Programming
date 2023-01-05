class Solution:
    def win(self, board, player):
        row_1 = board[0]
        row_2 = board[1]
        row_3 = board[2]
        
        col_1 = f"{row_1[0]}{row_2[0]}{row_3[0]}"
        col_2 = f"{row_1[1]}{row_2[1]}{row_3[1]}"
        col_3 = f"{row_1[2]}{row_2[2]}{row_3[2]}"
        
        diag_1 = f"{row_1[0]}{row_2[1]}{row_3[2]}"
        diag_2 = f"{row_1[2]}{row_2[1]}{row_3[0]}"
        
        player = player * 3
        
        if (row_1 == player or
            row_2 == player or 
            row_3 == player or
            col_1 == player or
            col_2 == player or
            col_3 == player or 
            diag_1 == player or
            diag_2 == player):
                return True
        
        return False
        
        
    def validTicTacToe(self, board: List[str]) -> bool:
        count_x = 0
        count_o = 0
        
        for row in board:
            for char in row:
                if char == "X":
                    count_x += 1
                elif char == "O":
                    count_o += 1        
                
        if self.win(board, "X") and self.win(board, "O"):            
            return False
        
        if count_x == count_o:                       
            if self.win(board, "X"):
                return False
            return True
        
        if count_x < count_o or count_x - count_o > 1:
            return False       
        
        if count_x - count_o == 1 and self.win(board, "O"):
            return False
            
        
        return True
        
        
                
        