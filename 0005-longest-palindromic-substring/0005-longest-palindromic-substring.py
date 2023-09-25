class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        
        max_length = 1
        
        substring = s[0]
        
        for gap in range(2, n + 1):
            for start in range(0, n - gap + 1):
                end = start + gap - 1
                
                if gap == 2:
                    if s[start] == s[end]:
                        dp[start][end] = 1
                        if gap > max_length:
                            max_length = gap
                            substring = s[start : end + 1]
                
                else:
                    if s[start] == s[end] and dp[start + 1][end - 1]:
                        dp[start][end] = 1
                        if gap > max_length:
                            max_length = gap
                            substring = s[start : end + 1]
        
        return substring
                