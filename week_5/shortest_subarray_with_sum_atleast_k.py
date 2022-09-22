"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""

import sys
from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [nums[0]] * (len(nums) + 1)
        
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        queue = deque()
        size = sys.maxsize
        for i, psum in enumerate(prefix_sum):            
            while queue and prefix_sum[queue[-1]] >= psum:                
                queue.pop()
                
            while queue and psum - prefix_sum[queue[0]] >= k:                
                size = min(size, i - queue.popleft())
                
            queue.append(i)            
        
        if size == sys.maxsize:
            return -1
        
        return size