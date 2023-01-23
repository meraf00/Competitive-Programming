"""https://codeforces.com/gym/421441/problem/D"""

def make_beautiful(grid):
    size = len(grid)
    flip_count = 0
    for layer in range((size)//2):        
        for top in range(size-1):
            right = top
            bottom = -top - 1
            left = -right - 1
            
            count = {0:0, 1:0}
            count[grid[layer][top]] += 1
            count[grid[-layer-1][bottom]] += 1
            count[grid[right][-layer-1]] += 1
            count[grid[left][layer]] += 1
            print(">>>", grid[layer], layer)
            flip_count += min(count.values())
    return flip_count

test_cases = int(input())

for _ in range(test_cases):
    grid_size = int(input())

    grid = []
    for _ in range(grid_size):
        row = list(map(int, list(input())))
        grid.append(row)
    
    print(">>>",make_beautiful(grid))
