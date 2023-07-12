class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        # (index of last element of seq, diff) : length of seq
        dp = {}
        
        for right in range(len(nums)):
            for left in range(right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1
        
        
        return max(dp.values())