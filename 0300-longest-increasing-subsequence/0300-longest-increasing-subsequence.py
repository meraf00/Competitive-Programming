class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1] * n
        
        ans = 1
        
        for i in range(n):
            for j in range(i - 1, -1, -1):                
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
                    ans = max(dp[i], ans)                
                    
        return ans