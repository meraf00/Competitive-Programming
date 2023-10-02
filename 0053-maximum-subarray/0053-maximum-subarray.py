class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)        
        
        max_sum = nums[0]
        
        for i in range(1, length):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            
            max_sum = max(nums[i], max_sum)
        
        return max_sum
        
        