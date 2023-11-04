class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = []
        
        for char in p:
            if char  == '*':
                if pattern[-1][-1] != '*':
                    c = pattern.pop()
                    pattern.append(f'{c}*')
            else:
                pattern.append(char)
        
        p = pattern   
        
        ns = len(s)
        np = len(p)
        
        
        dp = [[False] * (ns + 1) for _ in range(np + 1)]
        dp[0][0] = True
        
        
        for i in range(1, np + 1):            
            if len(p[i - 1]) == 2:                
                dp[i][0] = dp[i - 1][0]               
        
        
        for i in range(1, np + 1):
            for j in range(1, ns + 1):                
                if len(p[i - 1]) == 2:
                    char = p[i - 1][0]                
                    
                    if char == '.':
                        dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
                        
                    else:
                        dp[i][j] = (dp[i - 1][j - 1] or dp[i][j - 1]) and s[j - 1] == char or dp[i - 1][j]
                
                elif p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[j - 1] == p[i - 1]

            
        return dp[-1][-1]

"""
"aa"
"a"
"aa"
"a*"
"ab"
".*"
"aaa"
"ab*ac*a"
"si"
"s*"
"mississippi"
"mis*is*p*."
"abc"
"a***abc"
"""