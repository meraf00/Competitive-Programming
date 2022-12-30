class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        row_count = []
        for rx in range(rows):
            row_copy = []
            row_copy.extend(grid[rx])
            row_count.append(row_copy)
        
        diff = []
        for rx in range(rows):            
            diff.append([0] * cols)

        for rx in range(rows):
            for cx in range(cols):
                cell = grid[rx][cx]
                if cx != 0:
                    row_count[rx][cx] = row_count[rx][cx - 1] + cell
                if rx != 0:                    
                    grid[rx][cx] = grid[rx-1][cx] + cell
        
        for rx in range(rows):
            for cx in range(cols):                
                onesRow = row_count[rx][-1]
                onesCol = grid[-1][cx]
                zerosRow = rows - onesRow
                zerosCol = cols - onesCol
                                
                diff[rx][cx] = onesRow + onesCol - zerosRow - zerosCol
                                
        return diff
                
        