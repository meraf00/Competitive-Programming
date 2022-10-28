"""https://leetcode.com/problems/largest-number-at-least-twice-of-others"""

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = 0

        for i, n in enumerate(nums):
            if n > nums[max_index]:
                max_index = i
        
        for n in nums:
            if n != nums[max_index] and n * 2 > nums[max_index]:
                return -1
        return max_index