class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:         
        mod = pow(10, 9) + 7
        
        arrLen = min(arrLen, steps)
        
        dp = [[0] * (arrLen + 2) for _ in range(steps + 1)]
        
        dp[0][1] = 1                
        
        for i in range(1, steps + 1):            
            for j in range(1, arrLen + 1):
                dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
                
                dp[i][j] %= mod
                
                if dp[i][j] == 0:
                    break        
            
        return dp[-1][1] % mod