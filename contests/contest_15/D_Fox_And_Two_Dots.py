# https://codeforces.com/gym/442099/my

from collections import *
import sys

sys.setrecursionlimit(1000000)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


ENTER = 0
LEAVE = 1


def get_neighbours(pos):
    row, col = pos

    nbrs = []

    for dx, dy in directions:
        new_row = row + dy
        new_col = col + dx

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == grid[row][col]:
                nbrs.append((new_row, new_col))

    return nbrs


def has_cycle(curr, parent):
    visited.add(curr)

    for nbr in get_neighbours(curr):
        if nbr == parent:
            continue

        if nbr in visited or has_cycle(nbr, curr):
            return True

    return False


rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    grid.append(list(input()))


visited = set()
for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            if has_cycle((r, c), None):
                print("Yes")
                sys.exit()

print("No")
