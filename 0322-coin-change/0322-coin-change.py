class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n_coins = len(coins)
        
        dp = [float('inf')] * (amount + 1)
        
        # solution for 0 is always 0
        dp[0] = 0        
        
        
        for amount in range(amount + 1):
            for coin in coins:
                if coin <= amount:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]
                
                
                