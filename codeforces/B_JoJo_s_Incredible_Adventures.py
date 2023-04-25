# https://codeforces.com/problemset/problem/1820/B

# def draw_grid(string):
#     rows = cols = len(string)
#     grid = [[""] * cols for _ in range(rows)]    
    
#     for row in range(rows):
#         for col in range(cols):
#             if row == 0:
#                 grid[row][col] = string[col]
#             elif col == 0:
#                 grid[row][col] = string[row]
#             elif row >= col:
#                 grid[row][col] = string[row - col]
#             elif row < col:
#                 grid[row][col] = string[col - row]
    
#     return "\n".join(map(lambda row: "".join(row), grid))


def max_rect(string):
    length = len(string)
    string = string + string
    
    count = 0
    max_consecutive_ones = 0  

    for char in string:
        if char == '1':
            count += 1
        else:
            count = 0
        
        max_consecutive_ones = max(max_consecutive_ones, count)            
    
    if length < max_consecutive_ones:
        return length * length
    
    return ((max_consecutive_ones + 1) // 2) * ((max_consecutive_ones + 2) // 2)


test_cases = int(input())

for _ in range(test_cases):
    string = input()
    
    print(max_rect(string))