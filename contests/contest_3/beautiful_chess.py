"""https://codeforces.com/gym/421441/problem/C"""

test_cases = int(input())

def getBishop(board):  
    wide = False  
    for row_idx in range(8):       
        if board[row_idx].count("#") == 2:
            wide = True
        elif wide and board[row_idx].count("#") == 1:                
            return row_idx, board[row_idx].index("#")                

for _ in range(test_cases):
    # consume empty line
    input() 

    board = []
    for _ in range(8):
        board.append(input())    
    row, col = getBishop(board)

    print(row + 1, col + 1)

