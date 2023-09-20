class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n_arr = len(arr)
        
        dp = [0] * (n_arr + 1)
                        
        for i in range(n_arr + 1):
            for j in range(1, k + 1):
                if i - j < 0:
                    continue
                
                dp[i] = max(dp[i - j] + max(arr[i - j:i]) * j, dp[i])
                
        return dp[-1]