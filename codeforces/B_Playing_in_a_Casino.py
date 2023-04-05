# https://codeforces.com/problemset/problem/1808/B

def calculate_game_score(grid):
    rows, cols = len(grid), len(grid[0])

    total_sum = 0

    for row in range(rows):
        grid[row].sort()

        for col in range(cols):            
            # total_sum += col * grid[row][col] - (cols - col - 1) * grid[row][col]
            total_sum += (2 * col - cols + 1) * grid[row][col]
            
    
    return total_sum



test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())

    grid = []

    # transpose the input
    for row in range(m):
        grid.append([0] * n)

    for col in range(n):
        for row, num in enumerate(map(int, input().split())):
            grid[row][col] = num
        
            
    score = calculate_game_score(grid)
    print(score)
        