"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_of_zeros = 0
        left = 0
        right = 0                
        
        max_ones = 0
        while right < len(nums):
            if nums[right] == 0:
                num_of_zeros += 1                        
            
            while left < right and num_of_zeros > k:
                if nums[left] == 0:
                    num_of_zeros -= 1
                left += 1                                    
            
            if left == right:
                if nums[right] == 1 or k != 0:
                    max_ones = max(1, max_ones)                    
            else:
                max_ones = max(max_ones, right - left + 1)
            right += 1                        
            
        return max_ones