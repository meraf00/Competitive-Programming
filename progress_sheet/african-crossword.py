"""https://codeforces.com/problemset/problem/90/B"""

from collections import Counter


def solution(grid):
    rows = len(grid)
    cols = len(grid[0])
    grid_2 = []
    for row in grid:
        new_row = [x for x in row]
        grid_2.append(new_row)

    for row in grid:
        counter = Counter(row)
        for i, char in enumerate(row):
            if counter[char] > 1:
                row[i] = ""

    for col in range(cols):
        counter = {}
        for row in range(rows):
            if grid_2[row][col] in counter:
                counter[grid_2[row][col]] += 1
                continue
            counter[grid_2[row][col]] = 1
        for row in range(rows):
            if counter[grid_2[row][col]] > 1:
                grid[row][col] = ""

    output = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] and grid_2[row][col]:
                output.append(grid[row][col])

    return "".join(output)


n_rows, n_cols = list(map(int, input().split()))

grid = []
for _ in range(n_rows):
    row = list(input())
    grid.append(row)

print(solution(grid))
