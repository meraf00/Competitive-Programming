class Solution:                
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        computed = {0: cost[0], 1: cost[1]}
        
        def dp(stair_idx):
            if stair_idx in computed:
                return computed[stair_idx]
            
            computed[stair_idx] = min(dp(stair_idx - 1), dp(stair_idx - 2)) + cost[stair_idx]
            
            return computed[stair_idx]
        
        
        return dp(len(cost) - 1)
        
        
        # return computed[len(cost) - 1]
        
        
        
        
        
        
        
        
        