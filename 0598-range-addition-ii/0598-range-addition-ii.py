class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        
        for row, col in ops:
            min_row = min(row, min_row)
            min_col = min(col, min_col)
        
        return min_row * min_col
