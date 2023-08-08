class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_min = 0
        current_max = 0
        
        global_min = nums[0]
        global_max = nums[0]
        
        total_sum = 0        
        
        for num in nums:
            current_max = max(num, current_max + num)
            global_max = max(current_max, global_max)
            
            current_min = min(num, current_min + num)
            global_min = min(current_min, global_min)
            
            total_sum += num
        
        
        if total_sum == global_min:
            return global_max
        
        return max(global_max, total_sum - global_min)
        
        
       