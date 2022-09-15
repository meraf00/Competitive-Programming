"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""

import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        copy = []
        for row in matrix:
            for col in row:                 
                heapq.heappush(copy, col)
        
        while k > 0:            
            kth_smallest = heapq.heappop(copy)
            k -= 1
        
        return kth_smallest