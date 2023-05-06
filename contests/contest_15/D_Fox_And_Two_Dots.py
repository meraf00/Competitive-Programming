from collections import *
import sys

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]


ENTER = 0
LEAVE = 1

def get_neighbours(pos):    
    row, col = pos

    nbrs = []

    for dx, dy in directions:
        new_row = row + dy
        new_col = col + dx

        if 1 <= new_row <= rows and 1 <= new_col <= cols:
            if grid[new_row][new_col] == grid[row][col]:
                nbrs.append((new_row, new_col))
    
    return nbrs


def has_cycle(curr):
    r, c = curr

    grid[r][c] = ENTER

    for nbr in get_neighbours(curr):
        nbr_r, nbr_c = nbr
        if grid[nbr_r][nbr_c] == ENTER or has_cycle(nbr) :
            return True
    
    grid[r][c] = LEAVE
    
    return False

rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    grid.append(list(input()))


visited = set()
for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            if has_cycle((r, c)):
                print("Yes")
                sys.exit()

print("No")


