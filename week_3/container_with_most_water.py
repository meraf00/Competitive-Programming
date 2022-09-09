from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_volume = 0
        
        while left < right:            
            max_volume = max(max_volume, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:                
                left += 1
            else:
                right -= 1
                
        return max_volume