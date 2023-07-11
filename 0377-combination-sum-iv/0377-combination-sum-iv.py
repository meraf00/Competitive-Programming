class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        
        dp[0] = 1   # we have 1 way of reaching sum zero (taking no element)
        
        for i in range(target):
            # unreachable sum
            if dp[i] == 0:
                continue
                
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        
        return dp[target]