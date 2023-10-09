class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        
        dp = [0] * n
        
        i, j = 0, 1
        
        while j < n:
            if s[i] == s[j]:
                dp[j] = i + 1
                i += 1
                j += 1
            
            else:
                if i == 0:
                    j += 1
                
                else:
                    i = dp[i - 1]
                                                   
        return s[:dp[-1]]