class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        length = len(nums)
        
        left = 0
        
        max_length = 0                
        
        for right in range(length):
            # left should be even
            if nums[left] & 1:
                if nums[right] & 1:
                    continue                
                else:
                    left = right
                                    
            # have same parity
            if right > 0 and nums[right] % 2 == nums[right - 1] % 2:
                left = right  
            
            # the threshold
            if nums[right] > threshold:
                left = right + 1
                        
            
            max_length = max(right - left + 1, max_length)                
                
        return max_length
            
            
            
            