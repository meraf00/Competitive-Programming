from collections import deque

directions = [
    (0, 1), 
    (1, 0),
    (-1, 0),
    (0, -1)    
]

mouse_moves = {
    0: (0, 0),
    1: (0, -1),
    2: (0, 1),
    3: (-1, 0),
    4: (1, 0)
}

def get_neighbours(coord):    
    row, col = coord

    neighbours = []
    for dx, dy in directions:
        new_row = row + dy        
        new_col = col + dx

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
            neighbours.append((new_row, new_col))
        
    
    return neighbours


rows, cols, p = map(int, input().split())

grid = []

start_pos = None
for r in range(rows):
    row = []    
    for c, char in enumerate(input()):
        if char in '#':
            row.append(char)
        elif char == '.':
            row.append(float('-inf'))
        else:
            start_pos = (r, c)
            row.append(0)
    grid.append(row)

moves = map(int, input().split())


current_pos = start_pos
for i, move in enumerate(moves):
    r, c = current_pos
    dx, dy = mouse_moves[move]
    
    r += dy
    c += dx

    grid[r][c] = i + 1
    current_pos = (r, c)

r, c = current_pos
queue = deque([(current_pos, grid[r][c])])
# for row in range(rows):
#     for col in range(cols):        
#         if grid[row][col] != '#' and grid[row][col] != float('-inf'):
#             pos = (row, col)   
#             steps_left = grid[row][col]
#             queue.append((pos, steps_left))


while queue:
    pos, steps_left = queue.popleft()        
        
    if steps_left <= 0:
        continue

    curr_row, curr_col = pos
    
    for nbr in get_neighbours(pos):            
        r, c = nbr        
        if grid[r][c] < grid[curr_row][curr_col]:
            grid[r][c] = steps_left - 1
            queue.append((nbr, steps_left - 1))
    

count = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] not in ['#', float('-inf')]:
            count += 1

print(count)