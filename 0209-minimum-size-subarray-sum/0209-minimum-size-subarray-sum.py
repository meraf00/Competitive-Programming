class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        
        window_sum = 0
        min_size = float('inf')
        for right, num in enumerate(nums):
            window_sum += num
            
            while window_sum >= target:
                min_size = min(min_size, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
        if min_size == float('inf'):
            return 0
        
        return min_size
        