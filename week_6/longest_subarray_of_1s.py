"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""


from typing import List


class Solution:
    # not pretty
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = -1
        for i, n in enumerate(nums):
            if n == 1:
                left = right = i
                break

        if left == -1:
            return 0

        max_length = 0
        last_deleted = -1
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif left > last_deleted:
                last_deleted = right
                right += 1
            else:
                left = last_deleted + 1

            if last_deleted < left and ((left > 0 and nums[left-1] == 0) or (right < len(nums) and nums[right] == 0)):
                max_length = max(max_length, right - left)
            else:
                max_length = max(max_length, right - left - 1)

        return max_length
