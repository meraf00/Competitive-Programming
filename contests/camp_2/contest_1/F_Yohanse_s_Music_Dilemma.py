n_chairs, n_hours = map(int, input().split())

rows = 10 ** 2 + 1
cols = 10 ** 2 + 1
grid = [[0] * cols for _ in range(rows)]

chairs_coords = []

for _ in range(n_chairs):
    x, y = map(int, input().split())
    
    grid[x][y] += 1

for row in range(1, rows):
    grid[row][0] += grid[row - 1][0]

for col in range(1, cols):
    grid[0][col] += grid[0][col - 1]

for row in range(1, rows):
    for col in range(1, cols):
        grid[row][col] += grid[row - 1][col] + grid[row][col - 1] - grid[row - 1][col - 1]

def get_cell(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return grid[row][col]

    return 0

def get_sum(row1, col1, row2, col2):
    return get_cell(row2, col2) - get_cell(row1 - 1, col2) - get_cell(row2, col1 - 1) + get_cell(row1 - 1, col1 - 1)

for _ in range(n_hours):
    x1, y1, x2, y2 = map(int, input().split())
    
    print(get_sum(x1, y1, x2, y2))
