"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [i % 2 for i in nums]
        
        subarrays = 0
        left = right = 0
        odds = 0  
        last_left = last_right = 0
        while right < len(nums):
            odds += nums[right]
            
            if odds == k:
                last_right = right
                last_left = left
                while left <= right and nums[left] != 1:
                    left += 1
                right += 1
                while right < len(nums) and nums[right] != 1:
                    right += 1        
                
                subarrays += (left - last_left + 1) * (right - last_right)  
                                                
                if left < len(nums) and nums[left] == 1:
                    odds -= 1  
                
                left += 1
                right -= 1                 
            right += 1
        return subarrays