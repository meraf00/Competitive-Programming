class Solution:
    def isValid(self, seen, num):
        i = 0            
        while num:
            if num & 1:
                if seen & (1 << i):                        
                    return False                                        
            num >>= 1
            i += 1
            
        return True
                                
    def longestNiceSubarray(self, nums: List[int]) -> int:
        seen = 0
        
        left = 0
        
        max_length = 0
        
        for right, num in enumerate(nums):
            while left < right and not self.isValid(seen, num):
                seen ^= nums[left]
                left += 1
                            
            seen = seen | num
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
            
            
                        
                