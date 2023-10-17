class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        dp = [float('inf')] * (n + 1)
        
        dp[0] = 0
  
        day_pass = [1, 7, 30]
    
        for i in range(1, n + 1):
            for j, cost in enumerate(costs):                                
                
                day = days[i - 1] - day_pass[j] + 1
                
                m = bisect_left(days, day)
                
                for k in range(m, i):
                    dp[i] = min(dp[k] + cost, dp[i])

            
        return dp[-1]
                
                
                
        
        
        