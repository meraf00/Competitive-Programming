
directions = [
    (0, 1), 
    (1, 0),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]

def get_neighbours(coord):
    row, col = coord

    neighbours = []
    for dx, dy in directions:
        new_row = row + dy        
        new_col = col + dx

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:
            neighbours.append((new_row, new_col))
        
    
    return neighbours


test_cases = int(input())
rows = 2

for _ in range(test_cases):
    cols = int(input())

    grid = [
        list(map(int, input())),
        list(map(int, input()))    
    ]

    start = (0, 0)

    stack = [start]

    while stack:
        current = stack.pop()

        if current == (1, cols - 1):
            print("YES")
            break

        for nbr in get_neighbours(current):
            r, c = nbr
            grid[r][c] = 1
            stack.append(nbr)
    
    else:
        print("NO")









