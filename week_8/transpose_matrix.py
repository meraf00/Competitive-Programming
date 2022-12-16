from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        # create the matrix structure
        for i in range(n_cols):
            transposed.append([0] * n_rows)

        for rx in range(n_rows):
            for cx in range(n_cols):
                transposed[cx][rx] = matrix[rx][cx]

        return transposed
