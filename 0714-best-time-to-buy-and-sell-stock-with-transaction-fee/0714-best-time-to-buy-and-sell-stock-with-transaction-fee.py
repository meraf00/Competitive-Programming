class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # cash holding share
        hold = -prices[0]
        # cash without holding share
        free = 0
        
        for i in range(1, len(prices)):
            hold = max(hold, free - prices[i])
            
            free = max(free, prices[i] + hold - fee)
        
        return free
        