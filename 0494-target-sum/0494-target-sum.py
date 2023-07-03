class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if abs(target) > total:
            return 0
        
        dp = [[0] * (2 * total + 1)   for _ in range(len(nums))]
        
        dp[0][nums[0] + total] = 1
        dp[0][total - nums[0]] += 1
        
        
        for i in range(1, len(nums)):
            for s in range(-total, total + 1):
                if dp[i - 1][s + total] > 0:
                    dp[i][s + nums[i] + total] += dp[i - 1][s + total]
                    dp[i][s - nums[i] + total] += dp[i - 1][s + total]
        
        
        return dp[len(nums) - 1][target + total]