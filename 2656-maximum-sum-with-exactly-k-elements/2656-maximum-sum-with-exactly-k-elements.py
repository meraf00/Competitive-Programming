class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = max(nums)                
        
        return n * k + (k * (k - 1)) // 2