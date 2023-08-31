class Solution:
    def totalNQueens(self, n: int) -> int:                                        
        def is_valid(a, b):            
            for queen in solution:
                if queen == -1:
                    return True

                x, y = queen
                if x == a:
                    return False
                
                if abs((b - y) / (a - x)) == 1:
                    return False
                    
            return True
                    
            
        count = 0
        solution = [-1] * n
        
        def backtrack(col):        
            nonlocal count                        
            
            if col >= n:
                count += 1
                return                        
            
            for i in range(n):
                                
                if is_valid(i, col):
                    solution[col] = (i, col)
                    
                    backtrack(col + 1)
                    
                    solution[col] = -1                                    
        
        backtrack(0)
        return count
        
