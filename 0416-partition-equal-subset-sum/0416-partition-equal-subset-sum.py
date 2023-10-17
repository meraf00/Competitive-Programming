class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total & 1:
            return False
        
        n = len(nums)
        
        k = total // 2
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
                
        
        for i in range(1, n + 1):
            curr_val = nums[i - 1]
            
            for s in range(1, k + 1):
                if curr_val <= s:
                    dp[i][s] = max(curr_val + dp[i - 1][s - curr_val], dp[i - 1][s])
                
                else:
                    dp[i][s] = dp[i - 1][s]
                
                if dp[i][s] == k:                                        
                    return True
                 
        return False
                
                
            
        
        