class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n_nums = len(nums)
        total = sum(nums)
        
        target = total - x
        
        left = 0
        
        current_sum = 0                
        
        ops = float('inf')
        
        for right in range(n_nums):
            current_sum += nums[right]
            
            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:                
                ops = min(n_nums - (right - left + 1), ops)
        
        if ops == float('inf'):
            return -1
        
        return ops
            
            
            
        