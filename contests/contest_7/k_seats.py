
def get_cols(matrix, rows, cols):
    new = []
    for col in range(cols):
        col_ = []
        for row in range(rows):
            col_.append(matrix[row][col])
        new.append(col_)
    return new


def count_row(row, k):
    left = 0
    right = 0

    counter = 0
    while right < len(row):
        while right < len(row) and row[right] == "*":
            right += 1
            left = right

        if right - left + 1 == k:
            counter += 1
            left += 1

        right += 1
    return counter


def count_k_seats(grid, rows, cols, k):
    counter = 0
    for row in grid:
        counter += count_row(row, k)

    for row in get_cols(grid, rows, cols):
        counter += count_row(row, k)

    return counter


rows, cols, k=list(map(int, input().split()))

grid=[]
for _ in range(rows):
    row=input()
    grid.append(list(row))


print(count_k_seats(grid, rows, cols, k))

