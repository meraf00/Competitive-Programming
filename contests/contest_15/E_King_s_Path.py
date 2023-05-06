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

cols = rows = 10 ** 9

def get_neighbours(pos):    
    row, col = pos

    nbrs = []

    for dx, dy in directions:
        new_row = row + dy
        new_col = col + dx

        if 1 <= new_row <= rows and 1 <= new_col <= cols and (new_row, new_col) not in visited:
            for allowed_col in graph[new_row]:
                if new_col in allowed_col:
                    nbrs.append((new_row, new_col))
    
    return nbrs

a, b, c, d = map(int, input().split())
n = int(input())
start = (a, b)
target = (c, d)

graph = defaultdict(list)

for _ in range(n):
    row, l, r = map(int, input().split())

    graph[row].append(range(l, r + 1))

    
queue = deque([(start, 0)])

visited = set()

while queue:
    curr, path_length = queue.popleft()
    
    if curr == target:
        print(path_length)
        sys.exit()

    for nbr in get_neighbours(curr):
        if nbr not in visited:
            visited.add(nbr)
            queue.append((nbr, path_length + 1))

print(-1)


