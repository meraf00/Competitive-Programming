"""
https://leetcode.com/problems/find-pivot-index/
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        left = 0      
        
        for i, n in enumerate(nums):
            if left == total - left - n:
                return i
            left += n
        return -1