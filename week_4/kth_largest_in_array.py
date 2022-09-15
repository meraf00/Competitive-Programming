"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        
        while k > 0:
            kth_largest = heapq._heappop_max(nums)
            k -= 1
            
        return kth_largest