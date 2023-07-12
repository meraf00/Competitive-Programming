class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * n_glass for n_glass in range(1, 101)]                
        
        tower[0][0] = poured                
        
        for row_idx, row in enumerate(tower):
            if row_idx == 0:
                continue
                
            prev_row = tower[row_idx - 1]                        
            
            for glass_idx, val in enumerate(row):                
                if 0 < glass_idx < len(row) - 1:
                    left = 0 if prev_row[glass_idx - 1] <= 1 else prev_row[glass_idx - 1] - 1
                    right = 0 if prev_row[glass_idx] <= 1 else prev_row[glass_idx] - 1
                    
                    row[glass_idx] = left / 2 + right / 2
                
                elif glass_idx == 0:
                    overflow = 0 if prev_row[0] <= 1 else prev_row[0] - 1
                    row[glass_idx] = overflow / 2
                
                else:
                    overflow = 0 if prev_row[-1] <= 1 else prev_row[-1] - 1
                    row[glass_idx] = overflow / 2
                        
        
        return min(tower[query_row][query_glass], 1)