# https://codeforces.com/problemset/problem/3/C

def get_winner(board):
    # horiziontal
    if board[0] == board[1] == board[2] and board[0] != ".": return board[0]
    elif board[3] == board[4] == board[5] and board[5] != ".": return board[5]
    elif board[6] == board[7] == board[8] and board[6] != ".": return board[6]

    # diagonal
    elif board[0] == board[4] == board[8] and board[0] != ".": return board[0]
    elif board[2] == board[4] == board[6] and board[2] != ".": return board[2]

    # vertical
    elif board[0] == board[3] == board[6] and board[0] != ".": return board[0]
    elif board[1] == board[4] == board[7] and board[1] != ".": return board[1]
    elif board[2] == board[5] == board[8] and board[2] != ".": return board[2]

    
def check_state(board):    
    x_count = 0
    o_count = 0
    for cell in board:        
        if cell == "X":
            x_count += 1
        elif cell == "0":
            o_count += 1


    if x_count < o_count:
        return "illegal"
    
    move_count = x_count + o_count

    current_board = ["."] * 9            
    
    taken = set()    
    
    last_turn = "X"
    
    def backtrack(turn):
        nonlocal last_turn         
        
        if len(taken) == move_count and board == current_board:  
            last_turn = turn                      
            return True
        
        # pruning
        if len(taken) > move_count or len(taken) == 9 or get_winner(current_board):
            return                
    

        for i in range(9):            
            if i in taken:
                continue

            current_board[i] = turn
            taken.add(i)
            

            if backtrack("0" if turn == "X" else "X"):
                return True
            
            taken.remove(i)
            current_board[i] = "."

    
    
    if not backtrack(last_turn):
        return "illegal"
    
    winner = get_winner(board) 

    if not winner:
        if move_count == 9:
            return "draw"
        return "first" if last_turn == "X" else "second"    
    
    elif winner == "X":
        return "the first player won"
    
    elif winner == "0":
        return "the second player won"




board = []
for _ in range(3):
    board.extend(list(input()))

print(check_state(board))
