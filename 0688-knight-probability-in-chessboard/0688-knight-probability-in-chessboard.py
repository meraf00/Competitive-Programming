class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2)
        ]
        
        def isInbound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        def get_nbrs(row, col):
            nbrs = []
            
            for dx, dy in directions:
                new_row = row + dy
                new_col = col + dx
                
                if isInbound(new_row, new_col):
                    nbrs.append((new_row, new_col))
            
            return nbrs        
        
        @cache
        def dp(row, col, k):
            if k == 0:
                return isInbound(row, col)                    
            
            ans = 0
            
            for r, c in get_nbrs(row, col):
                ans +=  dp(r, c, k - 1)
            
            return ans
                    
        count = dp(row, column, k)
                
        return count / (8 ** k)
        
"""
8
30
6
4
"""        