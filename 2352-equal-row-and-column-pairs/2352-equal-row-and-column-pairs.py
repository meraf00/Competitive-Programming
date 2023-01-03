class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        
        for row in grid:
            val = []
            for col in row:
                val.append(str(col))
            
            row_concat = "-".join(val)
            rows[row_concat] += 1
        
        pair_count = 0
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        for c in range(n_cols):
            val = []
            for r in range(n_rows):
                val.append(str(grid[r][c]))
            
            col_concat = "-".join(val)
            pair_count += rows[col_concat]
        
        return pair_count
        