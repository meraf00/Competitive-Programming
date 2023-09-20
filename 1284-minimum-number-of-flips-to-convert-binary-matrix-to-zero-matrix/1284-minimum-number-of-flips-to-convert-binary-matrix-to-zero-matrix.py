class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        n_possible_comb = rows * cols
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        
        n_ones = 0
        
        for row in range(rows):
            for col in range(cols):
                n_ones += mat[row][col]
        
        def get_nbrs(row, col):
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    nbrs.append((new_row, new_col))
        
            return nbrs
                
        
        def flip(row, col):    
            nonlocal n_ones            
            
            for r, c in [(row, col)] + get_nbrs(row, col):
                if mat[r][c] == 0:
                    mat[r][c] = 1
                    n_ones += 1
                
                else:
                    mat[r][c] = 0
                    n_ones -= 1
        
        
        min_steps = float('inf')                
        
        def backtrack(n, flip_count): 
            nonlocal min_steps
            
            row = n // cols
            col = n % cols   
            
            if n_ones == 0:
                min_steps = min(min_steps, flip_count)
                return
            
            if row >= rows or col >= cols:                                 
                return
                                    
            # flip
            flip(row, col)            
            backtrack(n + 1, flip_count + 1)
            flip(row, col)
            
            # don't flip
            backtrack(n + 1, flip_count)
        
        backtrack(0, 0)
        
        if min_steps == float('inf'):
            return -1
        
        return min_steps
       