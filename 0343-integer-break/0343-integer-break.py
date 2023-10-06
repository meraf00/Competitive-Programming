class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        dp[1] = dp[2] = 1        
        
        for i in range(3, n + 1):
            for j in range(i - 1, 0, -1):
                k = i - j
                
                dp[i] = max(dp[i], j * k, dp[j] * dp[k], dp[j] * k, dp[k] * j)
                        
        return dp[-1]