class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n_coins = len(coins)
        
        dp = [[0] * (amount + 1) for _ in range(n_coins)]
        
        for row in range(n_coins):
            dp[row][0] = 1
        
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1
                
        for coin_idx in range(1, n_coins):
            current_coin = coins[coin_idx]
            
            for amt in range(1, amount + 1):
                num = amt - current_coin
                
                if num >= 0:
                    dp[coin_idx][amt] += dp[coin_idx - 1][amt] + dp[coin_idx][num]
                
                else:
                    dp[coin_idx][amt] += dp[coin_idx - 1][amt]
        
        
        return dp[-1][-1]
        
        