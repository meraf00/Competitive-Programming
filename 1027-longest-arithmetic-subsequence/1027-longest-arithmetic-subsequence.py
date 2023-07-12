class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        # (index of last element of seq, diff) : length of seq
        dp = defaultdict(lambda: 1)
        
        max_seq = 0
        
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] -  nums[left]                
                
                dp[(right, diff)] = dp[(left, diff)] + 1
                
                max_seq = max(dp[(right, diff)], max_seq)
        
        
        return max_seq