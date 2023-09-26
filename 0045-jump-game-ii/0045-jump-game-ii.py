class Solution:
    def jump(self, nums: List[int]) -> int:
        n_nums = len(nums)
        
        min_jump = [float('inf')] * n_nums
        min_jump[0] = 0
        
        for i in range(n_nums):
            
            for j in range(i + 1, nums[i] + i + 1):                
                if j >= n_nums:
                    break
                    
                min_jump[j] = min(min_jump[j], min_jump[i] + 1)
            
        return min_jump[-1]