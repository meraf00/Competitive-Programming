"""
https://leetcode.com/problems/minimum-size-subarray-sum/
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        min_size = len(nums) + 1

        left = 1
        right = 1
        while right < len(prefix):
            if prefix[right] - prefix[left-1] >= target:
                min_size = min(right - left + 1, min_size)
                left += 1
            else:
                right += 1

        return 0 if min_size == len(nums) + 1 else min_size
