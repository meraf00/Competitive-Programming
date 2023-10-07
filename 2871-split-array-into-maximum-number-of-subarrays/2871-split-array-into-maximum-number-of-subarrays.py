class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:        
        count = 0
                
        current_and = 0xffffffff 
        
        total = 0xffffffff
        
        for n in nums:
            current_and = current_and & n
            
            total = total & n
                        
            if current_and == 0:
                count += 1
                current_and = 0xffffffff
        
        
        if total != 0:
            return 1
        
        return count
