"""https://codeforces.com/contest/1676/problem/D"""

from collections import defaultdict

def get_right_diag_sums(board):
    rows = len(board)
    cols = len(board[0])

    diag_sum = defaultdict(int)

    for row_idx in range(rows):
        for col_idx in range(cols):
            diag_id = row_idx - col_idx
            num = board[row_idx][col_idx]
            diag_sum[diag_id] += num
    
    return diag_sum

def get_left_diag_sums(board):
    rows = len(board)
    cols = len(board[0])

    diag_sum = defaultdict(int)

    for row_idx in range(rows):
        for col_idx in range(cols):
            diag_id = row_idx + col_idx
            num = board[row_idx][col_idx]
            diag_sum[diag_id] += num
    
    return diag_sum

def get_maximum_attack_sum(board):
    left_diag_sum = get_left_diag_sums(board)
    right_diag_sum = get_right_diag_sums(board)

    max_sum = float('-inf')    
    for row_idx in range(rows):
        for col_idx in range(cols):
            left_id = row_idx + col_idx
            right_id = row_idx - col_idx            
            
            # x-sum is sum of left diag and right diag minus num at their intersection to account for duplicate addition
            num = board[row_idx][col_idx]
            x_sum = left_diag_sum[left_id] + right_diag_sum[right_id] - num
            max_sum = max(x_sum, max_sum)
    
    return max_sum


test_cases = int(input())

for _ in range(test_cases):
    rows, cols = map(int, input().split())
    
    board = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        board.append(row)
    
    max_sum = get_maximum_attack_sum(board)

    print(max_sum)
