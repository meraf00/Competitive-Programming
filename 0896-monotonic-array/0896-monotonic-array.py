class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sign = 0
        
        idx = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            
            if diff == 0:
                continue
            
            sign = diff // abs(diff)
            idx = i
            break
        
        
        for i in range(idx, len(nums)):
            diff = nums[i] - nums[i - 1]                        
            
            if diff == 0:
                continue
            
            if diff // abs(diff) != sign:
                return False
        
        return True
            
            
            
                
                