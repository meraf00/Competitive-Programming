class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
                    
        
        for gap in range(2, n + 1):
            for start in range(n - gap + 1):
                end = start + gap - 1     

                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2                      

                else:
                    dp[start][end] = max(
                        dp[start][end - 1], 
                        dp[start + 1][end],
                        dp[start + 1][end - 1])
        
        max_length = 1
        for row in dp:         
            max_length = max(max(row), max_length)
            
        return max_length
    
    
    
'''
"abcabcdaca"
'''