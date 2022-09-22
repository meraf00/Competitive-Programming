"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""

from typing import List
from collections import deque

class Solution:
    # required lots of help
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque() # keep track of candidate maximum values in window
        min_q = deque() # keep track of candidate minimum values in window
        
        left = 0
        max_size = 0
        for right, num in enumerate(nums):
            while max_q and nums[max_q[-1]] < num:
                max_q.pop()
            
            while min_q and nums[min_q[-1]] > num:
                min_q.pop()
            
            max_q.append(right)
            min_q.append(right)
            
            while min_q and max_q and nums[max_q[0]] - nums[min_q[0]] > limit:                
                if max_q[0] < min_q[0]:                    
                    left = max_q.popleft() + 1                
                else:
                    left = min_q.popleft() + 1
            
            max_size = max(max_size, right - left + 1)
        
        return max_size

    # TLE O(n^3) *~*
    def _longestSubarray(self, nums: List[int], limit: int) -> int:
        left = right = 0
        min_ = max_ = nums[0]
        max_size = 0
        while right < len(nums):
            min_ = min(min_, nums[right])
            max_ = max(max_, nums[right])
            
            while max_ - min_ > limit:
                min_ = min(nums[left + 1:right+1])
                max_ = max(nums[left + 1:right+1])
                max_size = max(max_size, right - left)
                left += 1                
            
            max_size = max(max_size, right - left + 1)            
            right += 1
            
        return max_size