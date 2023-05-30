class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        
        n_coins = len(coins)
                
                        
        def count_coins(left_amount):            
            if left_amount in memo:
                return memo[left_amount]                        
            
            min_count = float('inf')
            
            for coin in coins:
                
                if left_amount >= coin:                    
                    
                    count = 1 + count_coins(left_amount - coin)
                    
                    min_count = min(count, min_count)
                      
                        
            memo[left_amount] = min_count
            
            return memo[left_amount]
        
        
        min_coins = count_coins(amount)
        
        if min_coins == float('inf'):
            return -1
        
        return min_coins
        
        