class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        
        dp = [[0] * (lt + 1) for _ in range(ls + 1)]                
        
        for i in range(ls):
            dp[i][0] = 1
        
                
        for i in range(1, ls + 1):
            for j in range(1, lt + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] += dp[i - 1][j]
                

        
        return dp[-1][-1]
    #     r a b b i t
    # r   1 0 0 0 0 0
    # a   1 1 0 0 0 0
    # b   1 1 1 0 0 0    
    # b   1 1 2 1 0 0
    # b   1 1 3 3 0 0
    # i   1 1 3 3 3 0
    # t   1 1 3 3 3 0
    
    #     b a g
    # b   1 0 0
    # a   1 1 0
    # b   2 1 0
    # g   2 1 1
    # b   3 1 1
    # a   3 4 1
    # g   3 4 
        
        