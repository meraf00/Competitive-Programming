"""https://codeforces.com/gym/421441/problem/E"""


def findpath(board):
    rows = len(board)
    cols = len(board[0])
    
    start_pos = 0
    dest_post = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "S":
                start_pos = (i, j)
            elif board[i][j] == "T":
                dest_post = (i, j)
    
    # check horizontal
    row_start, col_start = start_pos
    start_left_bound = 0
    for i in range(row_start, -1, -1):
        if board[row_start][i] == "T":
            return True
        if board[row_start][i] == "*":
            start_left_bound = i + 1
            break

    start_right_bound = cols
    for i in range(row_start, cols):
        if board[row_start][i] == "T":
            return True
        if board[row_start][i] == "*":
            start_right_bound = i - 1
            break
            
    # check horizontal for destination
    row_dest, col_dest = dest_post
    dest_left_bound = 0
    for i in range(row_dest, -1, -1):        
        if board[row_dest][i] == "*":
            dest_left_bound = i + 1
            break

    dest_right_bound = cols
    for i in range(row_dest, cols):        
        if board[row_dest][i] == "*":
            dest_right_bound = i - 1
            break

    # check vertical        
    for i in range(col_start, -1, -1):
        if board[i][col_start] == "T":
            return True
        if board[i][col_start] == "*":
            break

    for i in range(col_start, rows):
        if board[i][col_start] == "T":
            return True
        if board[i][col_start] == "*":
            break
        
    # common
    left_b = max(start_left_bound, dest_left_bound)
    right_b = max(start_right_bound, dest_right_bound)
    for i in range(left_b, right_b):
        vertical_open = True
        for j in range(row_start, row_dest):
            if board[j][i] == "*":
                vertical_open = False
        
        if vertical_open:
            return True

    return False
    
    

rows, cols = map(int, input().split())
board = []

for _ in range(rows):
    row = input()
    board.append(row)

if findpath(board):
    print("YES")
else:
    print("NO")
