class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_volume = 0
        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            volume = (right - left) * min(left_height, right_height)
            
            max_volume = max(max_volume, volume)
            
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        
        return max_volume
                
        