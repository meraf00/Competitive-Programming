class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0                
        
        nums.append(float('inf'))        
        
        count = 0
        
        left = 0
        gap = nums[1] - nums[0]
        
        for right in range(1, len(nums)):
            g = nums[right] - nums[right - 1]
            
            if g != gap:
                n = right - left
                k = n - 3 + 1              
                count += k * (k + 1) // 2
                gap = g
                left = right - 1
                
        return count
        