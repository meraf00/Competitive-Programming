class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        cost.append(0)
        
        n = len(cost)
        
        dp = [0] * (n + 1)
        
        dp[1] = cost[0]
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 1])
                    
        return dp[-1]