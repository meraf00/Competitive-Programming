class Solution:
    def knightDialer(self, n: int) -> int:
        MODULO = 10 ** 9 + 7
        
        graph = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        # row - nth jump
        # col - ways to endup in cell
        dp = [[0] * 10 for _ in range(n)]                
        
        for i in range(10):
            dp[0][i] = 1
                        
        for k in range(1, n):
            for cell in range(10):
                for nbr in graph[cell]:
                    dp[k][nbr] += dp[k - 1][cell]                
        
        return sum(dp[-1]) % MODULO
        
        