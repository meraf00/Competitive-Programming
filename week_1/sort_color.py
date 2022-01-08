from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        red = 0
        white = 0
        blue = 0
        
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1 
            else:
                blue += 1
        
        i = len(nums) - 1
        
        while i >= 0:
            if blue:
                nums[i] = 2
                blue -= 1
            
            elif white:
                nums[i] = 1
                white -= 1
            
            else:
                nums[i] = 0
                red -= 1
            
            i -=  1
            
            
