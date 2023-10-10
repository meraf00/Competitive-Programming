class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        
        # dp[i][j] = max sum of ascii value of chars in equal strings
        # s1[:i] and s2[:j]
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + ord(s1[i - 1]))
                
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        
        total = 0
        
        for char in s1:
            total += ord(char)
        
        for char in s2:
            total += ord(char)
            
        return total - 2 * dp[-1][-1]
                    
                
        
        
        