class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        target = (n - 1, m - 1)
        
        memo = {}   
                            
        def dp(coord):
            x, y = coord            
            
            if coord in memo:
                return memo[coord]
            
            if coord == target:
                return 1
                        
            
            memo[coord] = 0
            
            if x + 1 < n:
                memo[coord] += dp((x + 1, y))
            
            if y + 1 < m:
                memo[coord] += dp((x, y + 1))
            
            return memo[coord]
        
        return dp((0, 0))
            
            
        