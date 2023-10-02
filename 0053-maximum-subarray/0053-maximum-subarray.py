class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        
        dp = nums[:]
        
        max_sum = dp[0]
        
        for i in range(1, length):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
            
            max_sum = max(dp[i], max_sum)
        
        return max_sum
        
        