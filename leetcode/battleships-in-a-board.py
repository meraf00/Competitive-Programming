class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X":
                    if row == 0 and col == 0:
                        count += 1
                    
                    elif row == 0:
                        if board[row][col - 1] == ".":
                            count += 1
                    
                    elif col == 0:
                        if board[row - 1][col] == ".":
                            count += 1
                                            
                    else:
                        if board[row - 1][col] == board[row][col - 1] == ".":
                            count += 1
            
        return count
                        