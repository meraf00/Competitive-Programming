"""
https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cummulative_left = [1] * len(nums)
        cummulative_right = [1] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                cummulative_left[i] = nums[i]
                cummulative_right[len(nums) - i - 1] = nums[len(nums) - i - 1]
                continue
            
            cummulative_left[i] = nums[i] * cummulative_left[i - 1]
            cummulative_right[len(nums) - i - 1] = nums[len(nums) - i - 1] * cummulative_right[len(nums) - i]
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = cummulative_right[i + 1]
                continue
            if i == len(nums) - 1:
                nums[i] = cummulative_left[i - 1]
                continue
            nums[i] = cummulative_left[i - 1] * cummulative_right[i + 1]        
        return nums
            
        